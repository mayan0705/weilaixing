<script>
export default {
};
</script>

<style>
  button {
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  }
  page {
    min-height: 100%;
    display: flex;
  }

  .content {
    display: flex;
    flex: 1;
    flex-direction: column;
    background-color: #F8F8F8;
  }

  .input-group {
    background-color: rgba(0, 0, 0, 0);
    margin: 2% auto;
    position: relative;
    width: 100%;
    border: 1px;
  }

  .input-row {
    display: flex;
    flex-direction: row;
    position: relative;
    border: 1px;
    border-color: black;
    padding: 5px;
    font-size: 18px;
    background-color: #ffffff;
    height: 30px;
    margin: 5px;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  }

  .input-row-top {
    display: flex;
    flex-direction: row;
    position: relative;
    border: 1px;
    border-color: black;
    padding: 5px;
    font-size: 18px;
    background-color: #ffffff;
    height: 30px;
    margin: 5px;
    margin-top: 20%;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  }
   
  .input-row-title,
  .input-row-short-title {
    width: 80px;
    text-align: justify;
  }

  .input-row-short-title {
    letter-spacing: 18px;
  }

  .vertification-btn {
    width: 105px;
    margin: 0 5px 0 100px;
    font-size: 15px;
    background-color: #efeff4;
    color: black;
    height: 30px;
    line-height: 30px;
  }

  .input-row-box-for-vertification {
    width: 200px;
    line-height: 30px;
    border: 1px;
    height: 30px;
  }

  .input-row-box-for-others {
    width: 200px;
    line-height: 30px;
    border: 1px;
    height: 30px;
  }
  
  .photo {
    display: flex;
    height: 120px;
    width: 120px;
    border-radius: 60px;
    margin: 20% auto 10%;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  }

  button:after {
    border: 0;
  }

  ul {
    list-style: none;
    margin: 5px auto;
    padding-left: 0;
    width: 90%;
  }
  
  .hasapplied-btn,
  .apply-btn,
  .refuse-btn {
    width: 50%;
    margin: 5% auto;
    height: 40px;
    line-height: 40px;
    color: white;
  }

  .apply-btn {
    background-color: lightgreen;
    box-shadow: 0 2px 4px 0 rgba(144, 238, 144, 0.1);
  }
  
  .hasapplied-btn {
    background-color: pink;
    box-shadow: 0 2px 4px 0 rgba(144, 238, 144, 0.1);
  }

  .refuse-btn {
    background-color: lightgray;
    box-shadow: 0 2px 4px 0 rgba(211, 211, 211, 0.1);
  }
</style>
