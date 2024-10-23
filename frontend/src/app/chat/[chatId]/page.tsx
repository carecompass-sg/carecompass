'use client';

import ChatMessage from "@/ui/chat/ChatMessage";
import { useRouter, useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";
import LoadingSpinner from "@/ui/loading";
import { useCurrentThreadStore } from "@/stores/currentThread";

export default function Chat({ params }: { params: { chatId: string }}) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const isNew = searchParams.get('new') === 'true'
  

  const [isLoading, setIsLoading] = useState(true);
  const currentThread = useCurrentThreadStore((state) => state.thread);
  currentThread.id = params.chatId;

  useEffect(() => {
    if (isNew) {
      setIsLoading(false);
      return
    }
    
    fetch(`${process.env.NEXT_PUBLIC_APP_BACKEND_URL}/threads/${params.chatId}/messages`)
      .then((response) => {
        if (response.ok) {
          response.json().then((data) => {
            useCurrentThreadStore.setState((state) => {
              return {
                thread: {
                  ...state.thread,
                  messages: data,
                },
              };
            });
          });
        } else {
          useCurrentThreadStore.getState().reset();
          router.replace("/chat");
        }
      })
      .catch((error) => {
        // TODO: Handle error
        console.error(error);
      })
      .finally(() => {
        setIsLoading(false);
      });
  }, [params.chatId, isNew]);

  useEffect(() => {
    if (!isLoading) {
      setTimeout(() => {
        const bottomMarker = document.getElementById("msg-bottom");
        if (bottomMarker) {
          bottomMarker.scrollIntoView();
        }
      }, 0); // A slight delay ensures rendering is done
    }
  }, [isLoading, currentThread.messages]);


  if (isLoading) {
    return <LoadingSpinner />;
  }

  return (
    <section className="flex flex-col gap-4 w-full h-[calc(100dvh-184px)] place-content-start overflow-y-auto">
      {currentThread.messages.map((message) => (
        <ChatMessage key={message.id} message={message} />
      ))}
      <div id="msg-bottom" />
    </section>
  );
}