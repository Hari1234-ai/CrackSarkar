"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { useUser } from "@/providers/user-context";

export default function StudyRedirect() {
  const router = useRouter();
  const { profile } = useUser();
  const exam = profile?.exam || "Group_II";

  useEffect(() => {
    router.replace(`/study/${exam}/subjects`);
  }, [exam, router]);

  return (
    <div className="flex items-center justify-center min-h-[60vh]">
      <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary"></div>
    </div>
  );
}
