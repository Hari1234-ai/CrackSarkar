"use client";

import React, { useEffect, useState } from "react";
import { ArrowRight, Trophy, Zap, AlertCircle } from "lucide-react";
import { DailyPlanCard } from "@/components/cards/DailyPlanCard";
import { ProgressChart } from "@/components/charts/ProgressChart";
import { StudyCard } from "@/components/cards/StudyCard";
import { getTodayPlan, getProgressOverview, getSyllabusTree } from "@/lib/api";
import { DailyPlan, UserProgressOverview, Paper } from "@/types";
import Link from "next/link";
import { motion } from "framer-motion";
import { cn } from "@/lib/utils";
import { useUser } from "@/providers/user-context";

function ExamCard({ id, title, description, papers, color, icon }: { 
  id: string, title: string, description: string, papers: number, color: string, icon: React.ReactNode 
}) {
  const colorMap: Record<string, string> = {
    indigo: "bg-indigo-50 border-indigo-200 text-indigo-700 dark:bg-indigo-950/20 dark:border-indigo-900/50 dark:text-indigo-400",
    purple: "bg-purple-50 border-purple-200 text-purple-700 dark:bg-purple-950/20 dark:border-purple-900/50 dark:text-purple-400",
    amber: "bg-amber-50 border-amber-200 text-amber-700 dark:bg-amber-950/20 dark:border-amber-900/50 dark:text-amber-400",
  };

  const accentMap: Record<string, string> = {
    indigo: "bg-indigo-600",
    purple: "bg-purple-600",
    amber: "bg-amber-600",
  };

  return (
    <Link href={`/study?exam=${id}`}>
      <motion.div 
        whileHover={{ y: -8, scale: 1.02 }}
        whileTap={{ scale: 0.98 }}
        className={cn(
          "relative group overflow-hidden p-8 rounded-[2rem] border-2 transition-all cursor-pointer h-full flex flex-col justify-between shadow-sm hover:shadow-xl",
          colorMap[color]
        )}
      >
        <div className="space-y-4">
          <div className={cn(
            "h-14 w-14 rounded-2xl flex items-center justify-center shadow-inner",
            accentMap[color], "text-white"
          )}>
            {icon}
          </div>
          <div className="space-y-1">
            <h3 className="text-2xl font-black tracking-tight leading-none">{title}</h3>
            <p className="text-sm font-medium opacity-80 leading-tight">{description}</p>
          </div>
        </div>
        
        <div className="mt-8 flex items-center justify-between">
          <div className="flex flex-col">
            <span className="text-2xl font-black leading-none">{papers}</span>
            <span className="text-[10px] font-bold uppercase tracking-widest opacity-60">Papers</span>
          </div>
          <div className={cn(
            "p-3 rounded-xl bg-white/20 dark:bg-black/20 backdrop-blur-sm group-hover:bg-white group-hover:text-black transition-all",
            "border border-white/30 dark:border-white/10"
          )}>
            <ArrowRight className="h-5 w-5" />
          </div>
        </div>

        {/* Decorative elements */}
        <div className="absolute -right-4 -bottom-4 h-24 w-24 rounded-full bg-current opacity-[0.03] group-hover:scale-150 transition-transform duration-700" />
      </motion.div>
    </Link>
  );
}

export default function Dashboard() {
  const { profile } = useUser();
  const selectedExamId = profile?.exam || "Group_II";
  const [todayPlan, setTodayPlan] = useState<DailyPlan | null>(null);
  const [progress, setProgress] = useState<UserProgressOverview | null>(null);
  const [syllabus, setSyllabus] = useState<Paper[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      setLoading(true);
      try {
        const [planData, progressData, syllabusData] = await Promise.all([
          getTodayPlan(selectedExamId),
          getProgressOverview(selectedExamId),
          getSyllabusTree(selectedExamId)
        ]);
        setTodayPlan(planData);
        setProgress(progressData);
        setSyllabus(syllabusData);
      } catch (error) {
        console.error("Error fetching dashboard data:", error);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, [selectedExamId]);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary"></div>
      </div>
    );
  }

  const todayTasks = todayPlan?.tasks.slice(0, 3) || [];
  const continueTopic = syllabus[0]?.subjects[0]?.topics[0];
  
  const chartData = [
    { subject: "History", progress: 45 },
    { subject: "Polity", progress: 30 },
    { subject: "Economy", progress: 20 },
    { subject: "Geography", progress: 65 },
    { subject: "Telangana", progress: 15 },
  ];

  return (
    <div className="space-y-12 pb-12 max-w-5xl mx-auto py-8">
      {/* Premium Welcome Header */}
      <div className="flex flex-col items-center text-center space-y-4">
         <motion.div 
           initial={{ scale: 0.9, opacity: 0 }}
           animate={{ scale: 1, opacity: 1 }}
           className="h-20 w-20 rounded-[2.5rem] bg-primary/10 flex items-center justify-center text-primary shadow-inner"
         >
            <Trophy className="h-10 w-10" />
         </motion.div>
         <motion.div
           initial={{ y: 20, opacity: 0 }}
           animate={{ y: 0, opacity: 1 }}
           transition={{ delay: 0.1 }}
         >
           <h1 className="text-5xl font-black tracking-tight text-foreground leading-tight">
             Good morning, <span className="text-primary">{profile?.name || "Aspirant"}</span>!
           </h1>
           <p className="text-xl text-muted-foreground mt-4 font-medium max-w-2xl mx-auto">
             Your educational journey continues today. Dive back into your syllabus and master every concept.
           </p>
         </motion.div>
      </div>

      {/* Target Path Section */}
      <motion.section 
        initial={{ y: 30, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ delay: 0.2 }}
        className="pt-8"
      >
        <div className="bg-card border-2 border-border/50 rounded-[3rem] p-12 relative overflow-hidden group">
           <div className="absolute top-0 right-0 p-8">
              <Zap className="h-12 w-12 text-primary/20 fill-primary/10" />
           </div>
           
           <div className="relative z-10 space-y-8">
              <div className="space-y-2">
                <span className="text-[10px] font-black uppercase tracking-[0.3em] text-primary bg-primary/10 px-4 py-2 rounded-full">Active Pathway</span>
                <h2 className="text-4xl font-black tracking-tight">{selectedExamId.replace("_", " ")}</h2>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-8 pt-4">
                 <Link href="/study" className="flex items-center justify-between p-8 bg-primary text-primary-foreground rounded-3xl hover:scale-[1.02] transition-all shadow-xl shadow-primary/20">
                    <div className="space-y-1">
                       <p className="text-lg font-black italic opacity-90 uppercase tracking-tighter">Enter Syllabus</p>
                       <p className="text-sm font-bold opacity-80">Start Study Session</p>
                    </div>
                    <ArrowRight className="h-8 w-8" />
                 </Link>

                 <div className="p-8 bg-secondary/30 border border-border/50 rounded-3xl flex items-center justify-center text-center italic text-muted-foreground font-medium">
                    "Success is the sum of small efforts, repeated day in and day out."
                 </div>
              </div>
           </div>

           {/* Decorative elements */}
           <div className="absolute -left-12 -bottom-12 h-64 w-64 rounded-full bg-primary/5 blur-3xl" />
        </div>
      </motion.section>
    </div>
  );
}

