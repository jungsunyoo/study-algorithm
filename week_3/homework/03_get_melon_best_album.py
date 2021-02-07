genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

class LinkedTuple:
    def __init__(self):
        self.items = list()
    def add(self,key,value):
        self.items.append((key,value))
    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v
    def sum(self):
        total = 0
        for k, v in self.items:
            total += v
        return total
    def largest_two(self):
        for i in range(len(self.items)):
            for j in range(i, self.items):
                if self.items[i][1] < self.items[j][1]:
                    self.items[i], self.items[j] = self.items[j], self.items[i]
        return self.items[0][0], self.items[1][0]




class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())
    def put(self, key1, key2, value):
        self.items[hash(key1) % len(self.items)].add(key2, value)
        # return
    def get(self, key1, key2):
        return self.items[hash(key1) % len(self.items)].get(key2)
    def len(self):
        return len(self.items)
    def call(self, value):
        return self.items[value]

def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    albums = LinkedDict()
    answer = []
    for i in range(len(genre_array)):
        albums.put(genre_array[i], i, play_array[i])

    # sort according to total values
    for i in range(albums.len()):
        for j in range(1, albums.len()):
            if albums.call(i).sum < albums.call(j).sum:
                albums[i], albums[j] = albums[j], albums[i]

    # select two indices within each genre that were listened to most
    for i in range(albums.len()):
        r1, r2 = albums[i].largest_two
        answer.append(r1)
        answer.append(r2)


    return answer


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!