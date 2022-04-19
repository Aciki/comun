<template>
  <div class="page-my-account">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My account</h1>
      </div>

      <div class="column is-12">
        <button @click="logout()" class="button is-danger">Log out</button>
      </div>

      <hr />

      <div class="columns is-multiline">
        <div class="column is-6">
          <div class="field">
            <label>First name*</label>
            <div class="control">
              <input type="text" class="input" v-model="first_name" />
            </div>
          </div>

          <div class="field">
            <label>Last name*</label>
            <div class="control">
              <input type="text" class="input" v-model="last_name" />
            </div>
          </div>

          <div class="field">
            <label>E-mail*</label>
            <div class="control">
              <input type="email" class="input" v-model="email" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import store from "../store";

// import OrderSummary from '@/components/OrderSummary.vue'
export default {
  name: "MyAccount",
  // components: {
  //     OrderSummary
  // },
      data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: []
        }
    },
  mounted() {
    //     const token = this.$store.state.token
    //     axios
    //    .get('/api/v1/auth/users/me/')
    //    .then(response => (this.profile = response))
    //     // axios.defaults.headers.common["Authorization"] = "Token " + token

    document.title = "My account | Djackets";
    this.getMyOrders();
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");
      this.$store.commit("removeToken");
      this.$router.push("/");
    },
    async getMyOrders() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("/api/v1/auth/users/me/")
        .then((response) => {
          this.orders = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>