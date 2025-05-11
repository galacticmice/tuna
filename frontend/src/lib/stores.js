import { writable } from "svelte/store";

const SESSION_STORAGE_KEY = 'llmResponseCache';

function getInitialCache() {
    if (typeof window !== 'undefined' && window.sessionStorage) {
        const storedCache = window.sessionStorage.getItem(SESSION_STORAGE_KEY);
        if (storedCache) {
            try {
                return JSON.parse(storedCache);
            } catch (e) {
                console.error("Error parsing cache from sessionStorage:", e);
                return {};
            }
        }
    }
    return {};
}

export const responseCache = writable(getInitialCache())

if (typeof window !== 'undefined' && window.sessionStorage) {
    responseCache.subscribe(value => {
        window.sessionStorage.setItem(SESSION_STORAGE_KEY, JSON.stringify(value));
    });
}