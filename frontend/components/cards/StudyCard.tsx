import React from "react";
import { BookOpen, CheckCircle, ChevronRight } from "lucide-react";
import { cn } from "@/lib/utils";

interface StudyCardProps {
  title: string;
  description?: string;
  progress: number;
  isCompleted?: boolean;
  onClick?: () => void;
  className?: string;
}

export function StudyCard({
  title,
  description,
  progress,
  isCompleted,
  onClick,
  className,
}: StudyCardProps) {
  return (
    <div
      onClick={onClick}
      className={cn(
        "group relative flex flex-col justify-between p-5 rounded-2xl border border-border bg-card hover:border-primary/50 transition-all cursor-pointer shadow-sm hover:shadow-md",
        isCompleted ? "opacity-70" : "",
        className
      )}
    >
      <div className="flex justify-between items-start mb-4">
        <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10 text-primary">
          {isCompleted ? <CheckCircle className="h-5 w-5" /> : <BookOpen className="h-5 w-5" />}
        </div>
        {!isCompleted && (
          <span className="text-xs font-medium text-muted-foreground bg-secondary px-2 py-1 rounded-md">
            {progress}% completed
          </span>
        )}
      </div>

      <div>
        <h3 className="font-semibold text-lg line-clamp-2 mb-1">{title}</h3>
        {description && <p className="text-sm text-muted-foreground line-clamp-2">{description}</p>}
      </div>

      <div className="mt-6 flex items-center justify-between">
        <div className="flex-1 mr-4">
          <div className="h-2 w-full bg-secondary rounded-full overflow-hidden">
            <div
              className="h-full bg-primary transition-all duration-500 ease-out"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>
        <ChevronRight className="h-5 w-5 text-muted-foreground group-hover:text-primary transition-colors" />
      </div>
    </div>
  );
}
