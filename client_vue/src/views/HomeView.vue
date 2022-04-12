<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to Djacket
            </p>
            <p class="subtitle">
                The best jacket store online
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>
      

      <div class="column is-3" v v-for="news in latestNews"
      v-bind:key="news.id">
      <div class="box">
        <figure class="image mb-4">
          <img :src="news.get_thumbnail">
        </figure>
      </div>
      <h3 class="is-size-4">
        {{ news.title }}
      </h3>
     
      <p class="is-size-6 has-text-grey">{{ news.created_at }}</p>

      <router-link v-bind:to="news.get_absolute_url" class="button is-dark mt-4">View details</router-link>


      </div>
      

      <!-- <ProductBox 
        v-for="news in latestProducts"
        v-bind:key="news.id"
        /> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import ProductBox from '@/components/ProductBox'
export default {
  name: 'Home',
  data() {
    return {
      latestNews: []
    }
  },
  // components: {
  //   ProductBox
  // },
  mounted() {
    this.getLatestNews()
    document.title = 'Home | Komunalec'
  },
  methods: {
    async getLatestNews() {
      this.$store.commit('setIsLoading', true)
      await axios
        .get('/all/')
        .then(response => {
          this.latestNews = response.data
        })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>
