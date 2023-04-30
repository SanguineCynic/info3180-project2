<script lang="ts">
export default {
  name: 'Register',
  data() {
    return {
      imageSrc: 'https://via.placeholder.com/350x550',
    };
  }
}
</script>

<template>
    <div class="registration">
      <h1>Register</h1>
      <form>
        <div class="form-group" >
          <label for="username">Username</label>
          <input id="username" type="text"  required>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input id="password" type="password" required>
        </div>
        <div class="form-group">
          <label for="firstname">First Name</label>
          <input id="firstname" type="text" required>
        </div>
        <div class="form-group">
          <label for="lastname">Last Name</label>
          <input id="lastname" type="text" required>
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input id="email" type="email" required>
        </div>
        <div class="form-group">
          <label for="location">Location</label>
          <input id="location" type="text" required>
        </div>
        <div class="form-group">
          <label for="biography">Biography</label>
          <textarea id="biography"></textarea>
        </div>
        <div class="form-group">
          <label for="photo">Photo</label>
          <input id="photo" type="file" accept="image/jpeg,image/png" @change="handlePhotoUpload" required>
        </div>
        <button type="submit" class="register-button">Register</button>
      </form>
    </div>
  </template>
  
  
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
  