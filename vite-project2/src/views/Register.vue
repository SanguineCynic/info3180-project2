<template>
    <div class="registration">
      <h1>Register</h1>
      <form>
        <div class="form-group">
          <label for="username">Username</label>
          <input id="username" type="text" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input id="password" type="password" v-model="password" required>
        </div>
        <div class="form-group">
          <label for="firstname">First Name</label>
          <input id="firstname" type="text" v-model="firstname" required>
        </div>
        <div class="form-group">
          <label for="lastname">Last Name</label>
          <input id="lastname" type="text" v-model="lastname" required>
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input id="email" type="email" v-model="email" required>
        </div>
        <div class="form-group">
          <label for="location">Location</label>
          <input id="location" type="text" v-model="location" required>
        </div>
        <div class="form-group">
          <label for="biography">Biography</label>
          <textarea id="biography" v-model="biography"></textarea>
        </div>
        <div class="form-group">
          <label for="photo">Photo</label>
          <input id="photo" type="file" accept="image/jpeg,image/png" @change="handlePhotoUpload" required>
        </div>
        <button type="submit" class="register-button">Register</button>
      </form>
    </div>
  </template>
  
  <script lang="ts">
import { defineComponent } from 'vue';

  export default {
    data() {
      return {
        username: '',
        password: '',
        firstname: '',
        lastname: '',
        email: '',
        location: '',
        biography: '',
        photo: null
      };
    },
    methods: {
      handlePhotoUpload(event) {
        this.photo = event.target.files[0];
      }
    }
  }
  </script>
  
  <style>
  .registration {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
  }
  
  label {
    font-weight: bold;
    margin-bottom: 5px;
  }
  
  input[type="text"],
  input[type="password"],
  input[type="email"],
  textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .register-button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #00cc00;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .register-button:hover {
    background-color: #009900;
  }
  </style>
  