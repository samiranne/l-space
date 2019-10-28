<template>
  <div id="book-table">
    <table>
      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import {APIService} from '../services/apiService'
const apiService = new APIService()

export default {
  name: 'book-table',
  data () {
    return {
      books: []
    }
  },
  methods: {
    getBooks () {
      apiService.get('books').then(books => { this.books = books })
    }
  },
  mounted () {
    this.getBooks()
  }
}
</script>

<style scoped></style>
