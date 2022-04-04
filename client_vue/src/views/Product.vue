<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="news.get_image">
                </figure>

                <h1 class="title">{{ news.title }}</h1>
                <p>{{ news.price }}</p>
                 <br/>

                <p>{{ news.descripton }}</p>
               
                
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Information</h2>

                <p><strong>Price: </strong>${{ news.price }}</p>

                <div class="field has-addons mt-6">
                    <div class="control">
                        <input type="number" class="input" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart()">Add to cart</a>
                    </div>
                </div> 
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name: 'News',
    data() {
        return {
            news: {},
            quantity: 1
        }
    },
    mounted() {
        this.getNews() 
    },
    methods: {
        async getNews() {
            this.$store.commit('setIsLoading', true)
            // const category_slug = this.$route.params.category_slug
            const slug = this.$route.params.slug
            await axios
                .get(`${slug}`)
                .then(response => {
                    this.news = response.data
                    document.title = this.news.title + ' | Komunalec'
                })
                .catch(error => {
                    console.log(error,slug)
                })
            
            this.$store.commit('setIsLoading', false)
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }
            const item = {
                news: this.news,
                quantity: this.quantity
            }
            this.$store.commit('addToCart', item)
            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }
}
</script>