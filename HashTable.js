function hashStringToInt(str, tableSize) {
    let hash = 17;
    // 소수를 값으로 지정함으로서 장점은 키를 잘 분산시킬 수 있다.

    for (let i=0; i<str.length; i++) {
        hash = (7 * hash * str.charCodeAt(i)) % tableSize;

        // charCodeAt() 메서드는 주어진 인덱스에 대한 UTF-16 코드를 나타내는 0부터 65535 사이의 정수를 반환한다.
    }

    return hash;
}

class HashTable {

    table = new Array(3);
    numItems = 0;

    resize = () => {
        const newTable = new Array(this.table.length * 2);
        this.table.forEach(item => { // forEach() 메서드는 주어진 함수를 배열 요소 각각에 대해 실행합니다.
            if (item) {
                item.forEach(([key, value]) => {
                    const idx = hashStringToInt(key, newTable.length);
                    if (newTable[idx]) {
                        newTable[idx].push([key, value]);
                    } else {
                        newTable[idx] = [[key, value]];
                    }
                });
            }
        });
        this.table = newTable;
    }

    // Collapse(충돌)가 발생할 때 어떻게 대처해야 하는가
    set_item = (key, value) => {
        this.numItems++;
        const loadFactor = this.numItems / this.table.length;
        if (loadFactor > .8) {
            //resize
            this.resize();
        }

        const idx = hashStringToInt(key, this.table.length);
        if (this.table[idx]) { // this.table[idx]에 이미 값이 존재할 때
            this.table[idx].push([key, value]);
            console.log(this.table[idx])
        } else {
            this.table[idx] = [[key, value]];
        }
    };

    get_item = (key) => {
        const idx = hashStringToInt(key, this.table.length);

        if (!this.table[idx]) { // Simple Error Checking
            return null;
        }
        console.log(this.table[idx])
        return this.table[idx].find(x => x[0] === key)[1]; // find() 메서드는 주어진 판별 함수를 만족하는 첫 요소 값 반환. 그런 요소가 없다면 undefined 반환.
        // 
    };

}



const myTable = new HashTable();
myTable.set_item("firstName", "bob");
console.log(myTable.table.length);
myTable.set_item("lastName", "Tim");
myTable.set_item("age", 23);
console.log(myTable.table.length);
myTable.set_item("birthday", "2000/07/21");
console.log(myTable.table);
console.log(myTable.get_item("firstName"));
console.log(myTable.get_item("lastName"));
console.log(myTable.get_item("age"));
console.log(myTable.get_item("birthday"));

// 출처: Ben Award 유튜브 (https://youtu.be/UOxTMOCTEZk)
