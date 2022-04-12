<template>
    <tr>
        <!-- <td><router-link :to="item.news.get_absolute_url">{{ item.news.name }}</router-link></td> -->
        <td>${{ item.news.price }}</td>
        <td>
            {{ item.quantity }}
            <a @click="decrementQuantity(item)">-</a>
            <a @click="incrementQuantity(item)">+</a>
        </td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete" @click="removeFromCart(item)"></button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        intialItem: Object
    },
    data () {
        return {
            item : this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.news.price
        }
    }
}
</script>