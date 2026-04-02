"use client";

import React, { useState } from "react";
import { motion } from "framer-motion";
import { cn } from "@/lib/utils";

interface FlashcardProps {
  front: string;
  back: string;
  topic?: string;
  className?: string;
}

export function Flashcard({ front, back, topic, className }: FlashcardProps) {
  const [isFlipped, setIsFlipped] = useState(false);

  return (
    <div 
      className={cn("w-full h-80 perspective-1000 cursor-pointer", className)}
      onClick={() => setIsFlipped(!isFlipped)}
    >
      <motion.div
        className="w-full h-full relative preserve-3d"
        animate={{ rotateY: isFlipped ? 180 : 0 }}
        transition={{ duration: 0.6, type: "spring", stiffness: 260, damping: 20 }}
        style={{ transformStyle: "preserve-3d" }}
      >
        {/* Front */}
        <div className="absolute inset-0 backface-hidden flex flex-col p-6 rounded-3xl border-2 border-border bg-card shadow-sm">
          {topic && (
            <span className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-auto">
              {topic}
            </span>
          )}
          <div className="flex-1 flex items-center justify-center text-center">
            <h3 className="text-xl md:text-2xl font-medium text-foreground">{front}</h3>
          </div>
          <span className="text-xs text-center text-muted-foreground mt-auto">
            Tap to flip
          </span>
        </div>

        {/* Back */}
        <div 
          className="absolute inset-0 backface-hidden flex flex-col p-6 rounded-3xl border-2 border-primary/20 bg-primary/5 shadow-sm"
          style={{ transform: "rotateY(180deg)", backfaceVisibility: "hidden" }}
        >
          <div className="flex-1 flex items-center justify-center text-center overflow-y-auto">
            <p className="text-lg md:text-xl text-foreground">{back}</p>
          </div>
        </div>
      </motion.div>
    </div>
  );
}
