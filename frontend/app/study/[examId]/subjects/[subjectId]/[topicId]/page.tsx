"use client";

import React, { useEffect, useState } from "react";
import { useUser } from "@/providers/user-context";
import { getSyllabusTree } from "@/lib/api";
import { 
  ArrowLeft, 
  ArrowRight, 
  GitBranch,
  GraduationCap
} from "lucide-react";
import Link from "next/link";
import { motion } from "framer-motion";
import { useParams } from "next/navigation";
import { cn } from "@/lib/utils";
import { subjectThemes, defaultTheme } from "@/lib/constants";

export default function SubtopicsGridPage() {
  const { profile } = useUser();
  const params = useParams();
  const examId = params.examId as string;
  const subjectId = params.subjectId as string;
  const topicId = params.topicId as string;
  
  const [hierarchy, setHierarchy] = useState<{ subject: any, topic: any } | null>(null);
  const [loading, setLoading] = useState(true);
  const selectedExamId = examId || profile?.exam || "Group_II";

  useEffect(() => {
    async function fetchData() {
      setLoading(true);
      try {
        const syllabus = await getSyllabusTree(selectedExamId);
        let foundSubject = null;
        let foundTopic = null;
        
        for (const paper of syllabus) {
          const sub = paper.subjects.find(s => s.id === subjectId);
          if (sub) {
            foundSubject = sub;
            foundTopic = sub.topics.find(t => t.id === topicId);
            break;
          }
        }
        setHierarchy({ subject: foundSubject, topic: foundTopic });
      } catch (error) {
        console.error("Error fetching sub-topics:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, [selectedExamId, subjectId, topicId]);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary"></div>
      </div>
    );
  }

  if (!hierarchy?.topic) {
    return (
      <div className="text-center py-20">
        <h2 className="text-2xl font-bold">Topic not found</h2>
        <Link href={`/study/${selectedExamId}/subjects/${subjectId}`} className="text-primary hover:underline">Return to subject</Link>
      </div>
    );
  }
  
  const theme = hierarchy.subject ? (subjectThemes[hierarchy.subject.title.toUpperCase()] || defaultTheme) : defaultTheme;
  const SubjectIcon = theme.icon;

  return (
    <div className="space-y-12 pb-12 max-w-7xl mx-auto py-4">
      <header className="space-y-6">
        <Link 
          href={`/study/${selectedExamId}/subjects/${subjectId}`} 
          className="inline-flex items-center gap-2 text-muted-foreground hover:text-primary transition-colors font-bold text-sm uppercase tracking-wider"
        >
          <ArrowLeft className="h-4 w-4" /> Back to {hierarchy.subject.title}
        </Link>
        <div className="space-y-2">
            <div className="flex items-center gap-2" style={{ color: theme.color }}>
                <SubjectIcon className="h-6 w-6" />
                <span className="text-xs font-black uppercase tracking-[0.2em]">{hierarchy.topic.title}</span>
            </div>
            <h1 className="text-5xl font-black tracking-tight">Technical Sub-topics</h1>
            <p className="text-xl text-muted-foreground max-w-2xl font-medium">
              We've broken down {hierarchy.topic.title} into refined sub-topics. Select one to start reading.
            </p>
        </div>
      </header>

      <div className="space-y-4">
        {hierarchy.topic.subtopics?.map((sub: any, i: number) => (
          <Link key={sub.id} href={`/study/${selectedExamId}/subjects/${subjectId}/${topicId}/${sub.id}`}>
            <motion.div 
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: i * 0.05 }}
              whileHover={{ x: 10 }}
              className="group p-6 rounded-2xl bg-card border border-border/50 hover:border-primary/40 transition-all shadow-sm flex items-center justify-between"
            >
              <div className="flex items-center gap-6">
                 <div 
                  className="h-10 w-10 rounded-full flex items-center justify-center font-black text-xs transition-colors"
                  style={{ backgroundColor: theme.bg, color: theme.color }}
                 >
                    {i + 1}
                 </div>
                 <h3 className="text-lg font-black group-hover:text-primary transition-colors" style={{ '--hover-color': theme.color } as any}>{sub.title}</h3>
              </div>
              <div className="flex items-center gap-4">
                 <span className="text-[10px] font-black uppercase tracking-widest opacity-50" style={{ color: theme.color }}>Deep Dive</span>
                 <div className="p-2 rounded-lg bg-secondary text-muted-foreground group-hover:bg-primary group-hover:text-primary-foreground transition-all">
                   <ArrowRight className="h-4 w-4" />
                 </div>
              </div>
            </motion.div>
          </Link>
        ))}
      </div>
    </div>
  );
}
