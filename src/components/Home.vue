<template>
    <div id="app" class="home-page">
      <div class="card left-card">
        <img :src="imageSrc" alt="Instagram clone image" />
      </div>
      <div class="card right-card">
        <h2 class="card-title">Sign up for Instagram</h2>
        <form class="signup-form">
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
          </div>
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required>
          </div>
          <button type="submit" class="btn btn-primary">Sign up</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  
  export const HomePage =  defineComponent({
    name: 'HomePage',
    data() {
      return {
        imageSrc: 'https://ysm-res.cloudinary.com/image/upload/c_fill,f_auto,q_auto:eco,w_525/v1/websites4/live-prod/myysm/communications-technology/photography-and-video/photo/iStock-178420433_312652_56070_v2.jpg',
      };
    },
  });
  
  export default HomePage;
  </script>
  
  <style>
  .home-page {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
  
  .card {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
  
  .left-card {
    margin-right: 20px;
  }
  
  .card-title {
    margin-bottom: 20px;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input[type='text'],
  input[type='email'],
  input[type='password'] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  button[type='submit'] {
    width: 100%;
    padding: 10px;
    border: none;
    border-radius: 5px;
    background-color: #0095f6;
    color: #fff;
    font-weight: bold;
    cursor: pointer;
  }
  </style>
  