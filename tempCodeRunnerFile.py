 if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle.moveUp()
            if event.key == pygame.K_s:
                left_paddle.moveDown()
            if event.key == pygame.K_UP:
                right_paddle.moveUp()
            if event.key == pygame.K_DOWN:
                right_paddle.moveDown()
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or pygame.K_s:
                left_paddle.vely=0
            if event.key == pygame.K_UP or pygame.K_DOWN:
                right_paddle.vely=0
