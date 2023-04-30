<script lang="ts">
export default {
  name: 'New Post',
  data() {
    return {
      imageSrc: 'https://via.placeholder.com/350x550',
    };
  }
}
</script>

<template>
    <div class="newpost">
      <h1>New Post</h1>
      <form>
        <div class="form-group">
          <label for="photo">Photo</label>
          <input id="photo" type="file" accept="image/jpeg,image/png" @change="handlePhotoUpload" required>
        </div>
        <div class="form-group">
          <label for="caption">Caption</label>
          <textarea id="caption"></textarea>
        </div>
        <button type="submit" class="login-button">Login</button>
      </form>
    </div>
  </template>
  
  
  <style>
  .login {
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
  textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .login-button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #00cc00;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .login-button:hover {
    background-color: #009900;
  }
  </style>
  