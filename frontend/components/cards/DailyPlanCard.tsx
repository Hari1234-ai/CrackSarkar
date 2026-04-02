import React from "react";
import { PlayCircle, CheckCircle2, Clock, BookOpen } from "lucide-react";
import { DailyTask } from "@/types";
import { cn } from "@/lib/utils";

interface DailyPlanCardProps {
  task: DailyTask;
  onAction?: (taskId: string) => void;
}

export function DailyPlanCard({ task, onAction }: DailyPlanCardProps) {
  const getIcon = () => {
    switch (task.type) {
      case "study": return <BookOpen className="h-5 w-5" />;
      case "practice": return <PlayCircle className="h-5 w-5" />;
      case "revision": return <Clock className="h-5 w-5" />;
      case "mock_test": return <PlayCircle className="h-5 w-5 text-red-500" />;
      default: return <BookOpen className="h-5 w-5" />;
    }
  };

  const getTypeColor = () => {
    if (task.completed) return "bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400";
    switch (task.type) {
      case "study": return "bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400";
      case "practice": return "bg-purple-100 text-purple-700 dark:bg-purple-900/30 dark:text-purple-400";
      case "revision": return "bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400";
      case "mock_test": return "bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400";
      default: return "bg-secondary text-secondary-foreground";
    }
  };

  return (
    <div className={cn(
      "flex p-4 gap-4 rounded-xl border bg-card items-start",
      task.completed ? "border-green-200 dark:border-green-900/50 opacity-70" : "border-border shadow-sm"
    )}>
      <div className={cn("p-2.5 rounded-lg shrink-0", getTypeColor())}>
        {task.completed ? <CheckCircle2 className="h-5 w-5" /> : getIcon()}
      </div>
      
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2 mb-1">
          <span className="text-[10px] uppercase font-bold tracking-wider text-muted-foreground bg-secondary px-1.5 py-0.5 rounded">
            {task.type}
          </span>
          <span className="text-xs text-muted-foreground font-medium flex items-center gap-1">
            <Clock className="w-3 h-3" /> {task.duration_minutes}m
          </span>
        </div>
        <h4 className={cn("font-medium text-sm md:text-base mb-1", task.completed && "line-through text-muted-foreground")}>
          {task.title}
        </h4>
        <p className="text-xs md:text-sm text-muted-foreground line-clamp-2">
          {task.description}
        </p>
      </div>

      <button 
        onClick={() => onAction && onAction(task.id)}
        className={cn(
          "shrink-0 text-sm font-medium px-4 py-2 rounded-lg transition-colors",
          task.completed 
            ? "bg-secondary text-muted-foreground hover:bg-secondary/80" 
            : "bg-primary text-primary-foreground hover:bg-primary/90"
        )}
      >
        {task.completed ? "Review" : "Start"}
      </button>
    </div>
  );
}
