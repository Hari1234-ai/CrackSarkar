"use client";

import React, { useState } from "react";
import { ChevronRight, ChevronDown, CheckCircle2, LayoutGrid, Award, BookOpen, Target } from "lucide-react";
import { Paper, Subject, Topic, Subtopic } from "@/types";
import { cn } from "@/lib/utils";

interface TopicNavigatorProps {
  papers: Paper[];
  onSelectItem: (item: Topic | Subtopic, type: "topic" | "subtopic") => void;
  selectedItemId?: string;
  selectedExamId: string;
  onSelectExam: (examId: string) => void;
}

export function TopicNavigator({ 
  papers, 
  onSelectItem, 
  selectedItemId,
  selectedExamId,
  onSelectExam
}: TopicNavigatorProps) {
  const [expandedPapers, setExpandedPapers] = useState<string[]>([]);
  const [expandedSubjects, setExpandedSubjects] = useState<string[]>([]);
  const [expandedTopics, setExpandedTopics] = useState<string[]>([]);
  const [isExamDropdownOpen, setIsExamDropdownOpen] = useState(false);

  const exams = [
    { id: "Group_II", title: "Group II Mastery", icon: <Award className="h-4 w-4" /> },
    { id: "Group_III", title: "Group III Mastery", icon: <Target className="h-4 w-4" /> },
    { id: "Group_IV", title: "Group IV Mastery", icon: <LayoutGrid className="h-4 w-4" /> },
  ];

  const currentExam = exams.find(e => e.id === selectedExamId) || exams[0];

  const handleExamChange = (id: string) => {
    onSelectExam(id);
    setIsExamDropdownOpen(false);
  };

  const togglePaper = (id: string) => setExpandedPapers(prev => 
    prev.includes(id) ? prev.filter(p => p !== id) : [...prev, id]
  );
  const toggleSubject = (id: string) => setExpandedSubjects(prev => 
    prev.includes(id) ? prev.filter(s => s !== id) : [...prev, id]
  );
  const toggleTopic = (id: string) => {
    // If no subtopics, select it directly
    const topic = papers.flatMap(p => p.subjects).flatMap(s => s.topics).find(t => t.id === id);
    if (topic && (!topic.subtopics || topic.subtopics.length === 0)) {
      onSelectItem(topic, "topic");
      return;
    }
    setExpandedTopics(prev => 
      prev.includes(id) ? prev.filter(t => t !== id) : [...prev, id]
    );
  };

  return (
    <div className="space-y-6">
      {/* Exam Selector Dropdown */}
      <div className="relative">
        <button
          onClick={() => setIsExamDropdownOpen(!isExamDropdownOpen)}
          className="w-full flex items-center justify-between p-3 bg-primary/5 hover:bg-primary/10 border border-primary/20 rounded-xl transition-all group"
        >
          <div className="flex items-center gap-3">
            <div className="h-8 w-8 rounded-lg bg-primary text-white flex items-center justify-center shadow-sm">
              {currentExam.icon}
            </div>
            <div className="text-left">
              <div className="text-[10px] font-black uppercase tracking-tighter opacity-50">Current Path</div>
              <div className="text-sm font-bold leading-none">{currentExam.title}</div>
            </div>
          </div>
          <ChevronDown className={cn("h-4 w-4 transition-transform", isExamDropdownOpen && "rotate-180")} />
        </button>

        {isExamDropdownOpen && (
          <div className="absolute top-full mt-2 left-0 w-full bg-card border border-border rounded-xl shadow-2xl z-50 overflow-hidden py-1">
            {exams.map((exam) => (
              <button
                key={exam.id}
                onClick={() => handleExamChange(exam.id)}
                className={cn(
                  "w-full flex items-center gap-3 p-3 text-left hover:bg-secondary transition-colors text-sm font-medium",
                  selectedExamId === exam.id ? "text-primary bg-primary/5" : "text-muted-foreground"
                )}
              >
                {exam.icon}
                {exam.title}
              </button>
            ))}
          </div>
        )}
      </div>

      <div className="space-y-1 pt-2 border-t border-border/50">
        <div className="text-[10px] font-black uppercase tracking-[0.2em] text-muted-foreground/60 mb-2 px-1">Syllabus Breakdown</div>
        {papers.map((paper) => (
          <div key={paper.id} className="mb-1">
            <button
              onClick={() => togglePaper(paper.id)}
              className={cn(
                "flex items-center gap-2 w-full text-left p-2 hover:bg-secondary rounded-lg transition-colors group",
                expandedPapers.includes(paper.id) && "bg-secondary/50"
              )}
            >
              {expandedPapers.includes(paper.id) ? (
                <ChevronDown className="h-4 w-4 text-muted-foreground shrink-0" />
              ) : (
                <ChevronRight className="h-4 w-4 text-muted-foreground shrink-0" />
              )}
              <span className="font-semibold text-sm truncate">{paper.title}</span>
            </button>
            
            {expandedPapers.includes(paper.id) && (
              <div className="ml-4 mt-1 border-l border-border pl-3 space-y-1">
                {paper.subjects.map((subject) => (
                  <div key={subject.id}>
                    <button
                      onClick={() => toggleSubject(subject.id)}
                      className="flex items-center gap-2 w-full text-left p-2 hover:bg-secondary rounded-lg transition-colors"
                    >
                      {expandedSubjects.includes(subject.id) ? (
                        <ChevronDown className="h-3 w-3 text-muted-foreground shrink-0" />
                      ) : (
                        <ChevronRight className="h-3 w-3 text-muted-foreground shrink-0" />
                      )}
                      <span className="font-medium text-sm truncate">{subject.title}</span>
                    </button>

                    {expandedSubjects.includes(subject.id) && (
                      <div className="ml-3 mt-1 border-l border-border pl-3 space-y-1">
                        {subject.topics.map((topic) => (
                          <div key={topic.id}>
                            <button
                              onClick={() => toggleTopic(topic.id)}
                              className={cn(
                                "flex items-center justify-between w-full text-left p-2 hover:bg-secondary rounded-lg transition-colors overflow-hidden",
                                (topic.subtopics && topic.subtopics.length > 0) ? "" : (selectedItemId === topic.id ? "bg-primary/10 text-primary font-medium" : "")
                              )}
                            >
                              <div className="flex items-center gap-2 overflow-hidden mr-2">
                                {(topic.subtopics && topic.subtopics.length > 0) ? (
                                  expandedTopics.includes(topic.id) ? (
                                    <ChevronDown className="h-3 w-3 text-muted-foreground shrink-0" />
                                  ) : (
                                    <ChevronRight className="h-3 w-3 text-muted-foreground shrink-0" />
                                  )
                                ) : (
                                  <BookOpen className="h-3 w-3 text-primary shrink-0" />
                                )}
                                <span className="text-sm truncate">{topic.title}</span>
                              </div>
                              <span className={cn(
                                "text-[10px] px-1.5 py-0.5 rounded shrink-0",
                                topic.weightage === "High" ? "bg-red-100 text-red-600 dark:bg-red-900/30" :
                                topic.weightage === "Medium" ? "bg-amber-100 text-amber-600 dark:bg-amber-900/30" :
                                "bg-blue-100 text-blue-600 dark:bg-blue-900/30"
                              )}>
                                {topic.weightage}
                              </span>
                            </button>

                            {expandedTopics.includes(topic.id) && topic.subtopics && topic.subtopics.length > 0 && (
                              <div className="ml-3 mt-1 pl-3 space-y-1">
                                {topic.subtopics.map((subtopic) => (
                                  <button
                                    key={subtopic.id}
                                    onClick={() => onSelectItem(subtopic, "subtopic")}
                                    className={cn(
                                      "flex items-center justify-between w-full text-left p-2 rounded-lg transition-colors text-xs",
                                      selectedItemId === subtopic.id 
                                        ? "bg-primary/10 text-primary font-medium" 
                                        : "text-muted-foreground hover:bg-secondary hover:text-foreground"
                                    )}
                                  >
                                    <span className="truncate mr-2">{subtopic.title}</span>
                                    {subtopic.progress === 100 && (
                                      <CheckCircle2 className="h-3 w-3 text-green-500 shrink-0" />
                                    )}
                                  </button>
                                ))}
                              </div>
                            )}
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
