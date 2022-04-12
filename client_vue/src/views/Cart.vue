<template>
  <div class="page-cart">
      <div class="columns is-multiline">
          <div class="column-is-12">
              <h1 class="title">
                  Cart
              </h1>
              <div class="column is-12 box">
                  <table class="table is-fullwidth" v-if="cartTotalLength">
                      <thead>
                          <tr>
                              <th>Title</th>
                              <th>Price</th>
                              <th>Nesto</th>
                          </tr>
                      </thead>
                      <tbody>
                          <CartItem
                            v-for="item in cart.items"
                            v-bind:key="item.id"
                            v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart" />
                           />
                      </tbody>

                  </table>
                  <p v-else> Nothin </p>
              </div>

          </div>

      </div>
  </div>
</template>


<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'
export default {
  name: "Cart",
  components :{
      CartItem
  },
  data (){
      return {
          cart:{
              items: []
          }
      }
  },
  mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.news.id !== item.news.id)
            
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
            
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.news.price * curVal.quantity
            }, 0)
        },
    }
}
</script>


