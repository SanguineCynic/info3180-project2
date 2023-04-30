<template>
    <div class="explore">
      <div class="card-list">
        <div v-for="(post, index) in posts" :key="index" class="card">
          <div class="card-header">
            <img :src="post.userHeadIcon" alt="User Head Icon" class="user-head-icon" />
            <span class="username">{{ post.username }}</span>
          </div>
          <div class="card-image">
            <img :src="post.image" alt="Post Image" class="post-image" />
          </div>
          <div class="card-description">
            {{ post.description }}
          </div>
          <div class="card-footer">
            <span class="likes">
              <i class="far fa-heart"></i> {{ post.likes }}
            </span>
            <span class="date">{{ post.date }}</span>
          </div>
        </div>
      </div>
      <div class="new-post">
        <button class="new-post-button">New Post</button>
      </div>
    </div>
  </template>
  
  <script lang="ts">
    import { defineComponent } from 'vue';
  
    interface Post {
      userHeadIcon: string;
      username: string;
      image: string;
      description: string;
      likes: number;
      date: string;
    }
  
    export const Explore = defineComponent({
      name: 'Explore',
      props: {
        posts: {
          type: Array as () => Post[],
          required: true
        }
      }
    });
  
    export default Explore;
  </script>
  
  <style>
    /* Add styles here */
  </style>
  