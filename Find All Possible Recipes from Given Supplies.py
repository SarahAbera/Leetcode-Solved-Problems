class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        #building the graph
        graph = defaultdict(list)
        indegree = [0] * len(recipes)
        supplies = set(supplies)
        for i in range(len(recipes)):
            ingredient = set(ingredients[i])
            supply = ingredient.intersection(supplies)
            dependency = ingredient - supply
            if dependency:
                for ingredient in dependency:
                    graph[ingredient].append((recipes[i],i))
                    indegree[i] += 1
             
        queue = deque()
        cooked_recipes = []
        for i in range(len(recipes)):
            if indegree[i] == 0:
                queue.append(recipes[i])

        while queue:
            cooked = queue.popleft()
            cooked_recipes.append(cooked)
            
            for ingredient in graph[cooked]:
                indegree[ingredient[1]] -= 1
                if indegree[ingredient[1]] == 0:
                    queue.append(ingredient[0])

        return cooked_recipes
