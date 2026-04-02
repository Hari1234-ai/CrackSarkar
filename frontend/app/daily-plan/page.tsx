"use client";

import React, { useEffect, useState } from "react";
import { DailyPlanCard } from "@/components/cards/DailyPlanCard";
import { getTodayPlan, updateProgress } from "@/lib/api";
import { DailyPlan, DailyTask } from "@/types";
import { CalendarDays, Clock, CheckCircle2, ChevronLeft, ChevronRight, Zap, Target } from "lucide-react";
import { cn } from "@/lib/utils";

export default function DailyPlanPage() {
  const [plan, setPlan] = useState<DailyPlan | null>(null);
  const [completedTasks, setCompletedTasks] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchPlan() {
      try {
        const data = await getTodayPlan();
        setPlan(data);
        setCompletedTasks(data.tasks.filter(t => t.completed).map(t => t.id));
      } catch (error) {
        console.error("Error fetching plan:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchPlan();
  }, []);

  const toggleTask = async (id: string) => {
    const task = plan?.tasks.find(t => t.id === id);
    if (!task) return;

    const isNowCompleted = !completedTasks.includes(id);
    
    try {
      await updateProgress(id, task.type, isNowCompleted);
      setCompletedTasks(prev => 
        isNowCompleted ? [...prev, id] : prev.filter(t => t !== id)
      );
    } catch (error) {
      console.error("Error updating task progress:", error);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary"></div>
      </div>
    );
  }

  const tasks = plan?.tasks || [];
  const totalMinutes = tasks.reduce((acc, t) => acc + t.duration_minutes, 0);
  const dailyProgress = tasks.length > 0 ? Math.round((completedTasks.length / tasks.length) * 100) : 0;

  return (
    <div className="max-w-4xl mx-auto space-y-12 pb-20">
      {/* Date Header */}
      <header className="flex flex-col items-center text-center space-y-4">
        <div className="flex items-center gap-4 text-muted-foreground group">
          <button className="p-2 hover:bg-secondary rounded-full transition-colors"><ChevronLeft className="h-5 w-5" /></button>
          <div className="flex items-center gap-2 font-bold text-sm uppercase tracking-[0.2em]">
            <CalendarDays className="h-4 w-4" />
            {plan?.date ? new Date(plan.date).toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' }) : "Loading..."}
          </div>
          <button className="p-2 hover:bg-secondary rounded-full transition-colors"><ChevronRight className="h-5 w-5" /></button>
        </div>
        <h1 className="text-5xl font-black tracking-tighter">Daily Mission</h1>
      </header>

      {/* Progress Stats */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <StatCard 
          icon={<Clock className="h-5 w-5 text-blue-500" />}
          label="Time Required"
          value={`${totalMinutes} mins`}
          subtext="Approximately 2.5 hours"
        />
        <StatCard 
          icon={<Target className="h-5 w-5 text-purple-500" />}
          label="Tasks Today"
          value={tasks.length.toString()}
          subtext={`${completedTasks.length} completed`}
        />
        <StatCard 
          icon={<Zap className="h-5 w-5 text-amber-500" />}
          label="Daily Progress"
          value={`${dailyProgress}%`}
          subtext="Almost there!"
        />
      </section>

      {/* Progress Bar */}
      <div className="space-y-4">
        <div className="flex justify-between items-end">
          <span className="text-sm font-black uppercase tracking-widest text-muted-foreground">Mastery Progress</span>
          <span className="text-2xl font-black text-primary">{dailyProgress}%</span>
        </div>
        <div className="h-4 w-full bg-secondary rounded-full overflow-hidden border border-border/50">
          <div 
            className="h-full bg-primary transition-all duration-1000 ease-in-out relative"
            style={{ width: `${dailyProgress}%` }}
          >
            <div className="absolute inset-0 bg-gradient-to-r from-transparent to-white/20 animate-shimmer" />
          </div>
        </div>
      </div>

      {/* Task List */}
      <section className="space-y-4">
        <h2 className="text-xl font-bold mb-6 flex items-center gap-2">
          Your Breakdown
          <div className="h-px flex-1 bg-border ml-4" />
        </h2>
        <div className="grid grid-cols-1 gap-4">
          {tasks.map((task) => (
            <div key={task.id} onClick={() => toggleTask(task.id)} className="cursor-pointer">
              <DailyPlanCard 
                task={{ ...task, completed: completedTasks.includes(task.id) }} 
                onAction={(id) => toggleTask(id)}
              />
            </div>
          ))}
        </div>
      </section>

      {/* Motivation Section */}
      <footer className="p-8 rounded-3xl border-2 border-dashed border-border bg-card text-center space-y-4">
        <h3 className="text-sm font-black uppercase tracking-[0.3em] text-muted-foreground">Focus for today</h3>
        <p className="text-xl font-medium italic italic-serif">
          "The best way to predict the future is to create it."
        </p>
      </footer>
    </div>
  );
}

function StatCard({ icon, label, value, subtext }: { icon: React.ReactNode, label: string, value: string, subtext: string }) {
  return (
    <div className="bg-card border border-border p-6 rounded-2xl shadow-sm space-y-2">
      <div className="flex items-center gap-2 mb-2">
        {icon}
        <span className="text-xs font-bold uppercase tracking-widest text-muted-foreground">{label}</span>
      </div>
      <div className="text-3xl font-black tracking-tight">{value}</div>
      <div className="text-xs text-muted-foreground">{subtext}</div>
    </div>
  );
}
