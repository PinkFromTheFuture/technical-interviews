package com.sem.test2;

/**
 * A playlist is considered a repeating playlist if any of the songs contain a
 * reference to a previous song in the playlist. Otherwise, the playlist will
 * end with the last song which points to null.
 * 
 * Implement a function IsRepeatingPlaylist that returns true if a playlist is
 * repeating or false if it is not. For example, the following code prints
 * "true" as both songs point to each other.
 */
public class Test2 {
    public static class Song {
        private final String name;

        private Song nextSong;

        public String getName() {
            return name;
        }

        public Song getNextSong() {
            return nextSong;
        }

        public void setNextSong(Song song) {
            this.nextSong = song;
        }

        public Song(String name) {
            this.name = name;
        }

        // If the single linked list contains a cycle then the
        // slow and fastpointers will point to same song (they meet)
        // On the other hand if fast will point to null or next node of
        // fast will point to null then the linked list does not
        // contain a cycle.
        public boolean isRepeatingPlaylist() throws Exception {
            Song fast = this;
            Song slow = this;

            while(fast != null && fast.getNextSong() != null)
            {
                fast = fast.getNextSong().getNextSong();
                slow = slow.getNextSong();
                
                // if fast and slow pointers are meeting then
                // the linked list is cyclic
                if(fast == slow)
                {
                    return true;
                }
            }

            return false;
        }
    }

    public static void main(String[] args) throws Exception {
        Song first = new Song("Hello");
        Song second = new Song("Eye of the tiger");

        first.setNextSong(second);
        second.setNextSong(first);

        System.out.println(first.isRepeatingPlaylist());
    }
}
