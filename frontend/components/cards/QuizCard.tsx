import React from "react";
import { HelpCircle, Clock, ChevronRight } from "lucide-react";
import { cn } from "@/lib/utils";

interface QuizCardProps {
  title: string;
  topic: string;
  questionCount: number;
  duration: number; // in minutes
  difficulty?: "Easy" | "Medium" | "Hard";
  onClick?: () => void;
  className?: string;
}

export function QuizCard({
  title,
  topic,
  questionCount,
  duration,
  difficulty = "Medium",
  onClick,
  className,
}: QuizCardProps) {
  const difficultyColors = {
    Easy: "text-green-600 bg-green-100 dark:bg-green-900/30 dark:text-green-400",
    Medium: "text-amber-600 bg-amber-100 dark:bg-amber-900/30 dark:text-amber-400",
    Hard: "text-red-600 bg-red-100 dark:bg-red-900/30 dark:text-red-400",
  };

  return (
    <div
      onClick={onClick}
      className={cn(
        "flex flex-col p-5 rounded-2xl border border-border bg-card hover:border-primary/50 transition-all cursor-pointer shadow-sm hover:shadow-md",
        className
      )}
    >
      <div className="flex justify-between items-start mb-2">
        <span className="text-xs font-semibold uppercase tracking-wider text-primary">
          {topic}
        </span>
        <span className={cn("text-xs font-medium px-2 py-1 rounded-md", difficultyColors[difficulty])}>
          {difficulty}
        </span>
      </div>

      <h3 className="font-semibold text-lg line-clamp-2 mb-4">{title}</h3>

      <div className="mt-auto flex items-center justify-between text-sm text-muted-foreground">
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-1.5">
            <HelpCircle className="h-4 w-4" />
            <span>{questionCount} Qs</span>
          </div>
          <div className="flex items-center gap-1.5">
            <Clock className="h-4 w-4" />
            <span>{duration}m</span>
          </div>
        </div>
        <ChevronRight className="h-5 w-5 hover:text-primary transition-colors" />
      </div>
    </div>
  );
}
