package com.sem.test1;

import java.util.Arrays;
import java.util.HashSet;
import java.util.stream.Stream;

/**
 * Implement the union method. When passed two arrays of names, it will
 * return an array containing the names that appear in either or both arrays.
 * 
 * The returned array should have no duplicates.
 * 
 * For example, calling
 * 
 * union(new string[]{'Ava', 'Emma', 'Olivia'}, new string[]{'Olivia',
 * 'Sophia', 'Emma'})
 * 
 * should return an array containing Ava, Emma, Olivia, and Sophia in any order.
 */
 
public class Test1 {

    public static void main(String[] args) throws Exception {
        String[] names1 = new String[] { "Ava", "Emma", "Olivia" };
        String[] names2 = new String[] { "Olivia", "Sophia", "Emma" };
    
        System.out.println(Arrays.toString(union(names1, names2))); 
    }

    public static String[] union(String[] names1, String[] names2) throws Exception {
        // I will just concatenate the arrays and then get the set of them,
        // which will take care of duplicates
        String[] concatenated_array = Stream.concat(Arrays.stream(names1), Arrays.stream(names2)).toArray(String[]::new);
        String[] names_array = new HashSet<String>(Arrays.asList(concatenated_array)).toArray(new String[0]);

        return names_array;
    }
}
