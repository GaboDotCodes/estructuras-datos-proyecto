from pygame import draw, image, transform, font

class Tree:
    def __init__(self, toShow):
        self.root = None
        self.toShow = toShow

    def getRoot(self):
        return self.root
    
    def add(self, temp, node):
        if temp == None: 
            return True
        
        if node.getCode()> temp.getCode(): # Realiza el recorrido por la derecha 
            if self.add(temp.getRight(), node):
                temp.setRight(node)

        if node.getCode()< temp.getCode(): # Realiza el recorrido por la izquierda 
            if self.add(temp.getLeft(), node):
                temp.setLeft(node)
    
    def addNode(self, node):
        if self.root == None:
            self.root = node
        else:
            self.add(self.root, node)

    def getHeightNode(self, temp = None):
        if temp.isLeaf():
            return 1
        leftHeight = self.getHeightNode(temp.getLeft()) if temp.getLeft() != None else 1
        rightHeith = self.getHeightNode(temp.getRight()) if temp.getRight() != None else 1
        return 1 + max(leftHeight, rightHeith)
    
    def getHeight(self):
        return self.getHeightNode(self.root)
    
    def getMaxWidth(self):
        maxWidth = 0
        nodesInLevel = 0
        queue = []
        if(self.root == None):
            return 0
        queue.append(self.root)
        while(len(queue) != 0):
            nodesInLevel = len(queue)
            maxWidth = max(maxWidth, nodesInLevel)
            while(nodesInLevel > 0):
                current = queue.pop(0);  
                if(current.getLeft() != None):  
                    queue.append(current.getLeft());  
                if(current.getRight() != None):  
                    queue.append(current.getRight());  
                nodesInLevel = nodesInLevel - 1;  
        return maxWidth;  
    
    def showTree(self, window, rect):
        draw.rect(window, (255, 0, 0), rect, 2)
        if self.root:
            x_step = rect.width / self.getMaxWidth()
            y_step = rect.height / self.getHeight()
            side_complete = min(y_step, x_step)
            side = side_complete * 0.5
            start_point = (rect.midtop[0] - side / 2, rect.midtop[1] + side * 0.5)
            self.showNodes(window, side, x_step, y_step, self.root, start_point)
            
    
    def showNodes(self, window, side, x_step, y_step, node, point):
        img = image.load(node.getImage())
        img_t = transform.scale(img, (side, side))
        window.blit(img_t, point)
        
        fontConfig = font.SysFont("Calibri", 18)
        labels = []
        labels.append(fontConfig.render('Codigo: {}'.format(node.getCode()), True, (255, 255, 255)))
        for property in self.toShow:
            labels.append(fontConfig.render('{}{}'.format(property[0], node.getData()[property[1]]), True, (255, 255, 255)))
        for line in range(len(labels)):
            window.blit(labels[line], (point[0] + side, point[1]+(line*18)+(5*line) ))
        
        startPoint = (point[0] + side / 2, point[1] + side)
        
        if node.getLeft() != None:
            finishLineL = (point[0] - x_step + side / 2, point[1] + y_step)
            draw.line(window, (255, 255, 255), startPoint, finishLineL, 2)
            
            leftPoint = (point[0] - x_step, point[1] + y_step)
            self.showNodes(window, side, x_step * 0.5, y_step, node.getLeft(), leftPoint)
        if node.getRight() != None:
            finishLineR = (point[0] + x_step + side / 2, point[1] + y_step)
            draw.line(window, (255, 255, 255), startPoint, finishLineR, 2)
            
            rightPoint = (point[0] + x_step, point[1] + y_step)
            self.showNodes(window, side, x_step * 0.5, y_step, node.getRight(), rightPoint)            
        
    def getList(self):
        return self.list

    def Recorrido1(self, padre):
        if padre == None:
            return
        
        self.Recorrido1(padre.getLeft())
        self.list.append(padre.getCode())
        self.Recorrido1(padre.getRight())
    