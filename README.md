# 노드생성

* create

```sql
CREATE (A: 회사{officeName: "A", CEO_Name:"AA"}) return A
```

* merge

```sql
MERGE (A: 회사{officeName: "A", CEO_Name:"AA"}) return A
```

CREATE는 무조건 새로운 노드를 생성하지만 MERGE는 전달된 속성들이 일치하는 노드가 있다면 새로운 노드를 생성하지 않음 앞의 MERGE는 officeName과 CEO_Name만 검사하여 노드 생성유무가 결정됨

# 노드삭제

* 전체노드 삭제

```sql
MATCH (n) DETACH DELETE n
```

# 노드조회

```sql
MATCH (n) return n
```

# 관계생성

* 직원 노드생성

```sql
MERGE (worker1:Worker{name: "직원1", age: 20}) return worker1
MERGE (worker2:Worker{name: "직원2", age: 30}) return worker2
MERGE (worker3:Worker{name: "직원3", age: 40}) return worker3
MERGE (worker4:Worker{name: "직원4", age: 50}) return worker4
```

* 회사 노드생성

```sql
MERGE (office1:Office{name: "office1"}) return office1
MERGE (office2:Office{name: "office2"}) return office2
```

* 관계형성

```sql
CREATE (worker:Worker{name: "직원1"}) - [:work] -> (office:Office{name: "office1"})
CREATE (worker:Worker{name: "직원2"}) - [:work] -> (office:Office{name: "office1"})
CREATE (worker:Worker{name: "직원3"}) - [:work] -> (office:Office{name: "office1"})

CREATE (worker:Worker{name: "직원3"}) - [:work] -> (office:Office{name: "office2"})
CREATE (worker:Worker{name: "직원4"}) - [:work] -> (office:Office{name: "office2"})
```

```sql
MERGE (worker:Worker{name: "직원1"}) - [:work] -> (office:Office{name: "office1"})
MERGE (worker:Worker{name: "직원2"}) - [:work] -> (office:Office{name: "office1"})
MERGE (worker:Worker{name: "직원3"}) - [:work] -> (office:Office{name: "office1"})

MERGE (worker:Worker{name: "직원3"}) - [:work] -> (office:Office{name: "office2"})
MERGE (worker:Worker{name: "직원4"}) - [:work] -> (office:Office{name: "office2"})
```

관계를 형성할 땐 CREATE나 MERGE난 각 노드의 존재보다 해당 관계가 없으면 새로운 노드를 생성하여 관계를 만든다

만약 기존에 존재하는 노드의 관계를 추가한다면 MATCH를 이용한다.

```sql
MATCH (worker1:Worker{name:'직원1'}), (worker2: Worker{name: 
"직원2"})  
CREATE (worker1) <- [:colleague] - (worker2)
return worker1, worker2
```

```sql
MATCH (worker1:Worker{name:'직원1'}), (worker2: Worker{name: 
"직원4"})  
MERGE (worker1) <- [:other] - (worker2)
return worker1, worker2
```

노드를 검색한 후 관계를 추가한다. 이 경우도 CREATE와 MERGE의 성격을 그대로 가져간다. CREATE는 노드간의 간선을 무조건 추가하지만 MERGE는 관계의 간선이 이미 존재한다면 생성하지 않는다.

```sql
MERGE (w1:Worker{name:"직원1"})
MERGE (w2:Worker{name:"직원2"})
MERGE (w1) <- [:colleague] - (w2)
return w1, w2
```

# 조회

```sql
MATCH (worker1:Worker{name:'직원1'}), (worker2: Worker{name: 
"직원4"})  
return worker1, worker2
```

```sql
MATCH(worker: Worker)
WHERE 
worker.name = "직원1" or worker.name = "직원4"
RETURN worker
```

이 둘의 결과 차이점은 크게 없어 보이나 데이터를 조회하는 성격에 따라 다르게 사용하면 될듯으로 보임

```sql
MATCH p = (:Worker) --> () 
RETURN p
```

Woker로 만들어진 모든 노드가 참조하는 노드들 조회

```sql
MATCH p = (:Worker) <-- () 
RETURN p
```

Woker로 만들어진 모든 노드를 참조하는 노드들 조회

```sql
MATCH p = (w: Worker{name:"직원1"})<--()
RETURN p
```

노드1을 참조하는 노드들 조회

```sql
MATCH p = (w: Worker{name:"직원1"})-->()
RETURN p
```

노드1이 참조하는 노드들 조회

```sql
MATCH (:Worker) - [r] -> (:Worker)
return type(r)
```

```sql
MATCH (:Worker) <- [r] - (:Worker)
return type(r)
```

```sql
MATCH p = (:Worker{name:"직원1"})<-[r]-()
return p, r, type(r)
```

관계정보 조회

```sql
MATCH p = (:Worker{name:"직원1"})-[r]->()
return p, r, type(r)
```

관계정보 조회
