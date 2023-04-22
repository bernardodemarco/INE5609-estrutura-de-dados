# Relatório T1 - Lista Duplamente Encadeada Com Cursor

Esse documento é o relatório do trabalho 1 da disicplina INE5609 feito pelo aluno Bernardo De Marco Gonçalves.

## Sumário

- [Sobre a documentação](#documentação-dos-métodos)
- [Diagrama de classes](#diagrama-de-classes)
- [Atributos classe Node](#atributos-node)
- [Atributos classe DoubleLinkedList](#atributos-doublelinkedlist)
- [Métodos](#métodos)

## Documentação dos métodos

A documentação dos métodos foi feita com [docstrings](https://peps.python.org/pep-0257/), seguindo o seguinte padrão:

```python
    def docs_pattern():
        """
        Breve descrição do método.

        Descrição mais detalhada do método caso seja necessária.

        Args:
            nome_parametro (tipo_parametro): descrição.

        Returns:
            tipo_retorno: descrição.

        Raises:
            Exceção: descrição.
        """
        pass
```

## Diagrama de classes

Para a implementação da lista duplamente encadeada com cursor foram implementadas duas classes, a DoubleLinkedList e a Node. Segue o diagrama de classes contendo os atributos e métodos delas.

[![Diagrama de classes](https://mermaid.ink/img/pako:eNqVVLFugzAQ_RXLE22ToStDp45ph3ZFshx8JFaMjexzmqjKv_fAkAIpVcuCeff8jnu-8ycvnQKe89LIEJ613HlZF5bRo7SHErWzbPOWkI7DXmnDZwIYWx-licByJu35ilk4IUEt8Yo1Ho7axTDBL2PdZxe3BjbaHkBtdMDvHAGlvxEsow_Oz1Eba-EqAQZqsNhm0xav0VqehAG7w_0sIMTOicr5D-mVOIjGBd1WHrJDIt5RFgtT-laWh__w0YmukGwhCFbdhvbSKgNC2wC-zSA-NO4F1A2ehSGTspH_080POiQeiW6dM2O8isbcwF0KsQWyAQS568nA3-QTX1YI_h907E34C7N15C-8wf5MWwWndAIrtrzTQ-2O3zXejZt3CFbah4UQdetCpG-7jCrcAQ65fyAu_PSUWzqLkqqcyU1OjfCFOtrIkINGYiYyav6OOXTmXCE15RxNM5RNZRpPX6kpx373Mz6fblbwx4Kz9fqJVve0aseYr3gNvpZa0Y3UzX_BcU-eFjynpYJKRoMFL-yFqDKiez_bkufoI6x4bJRE6O8wnlfSBEJBaXT-pb_l2tflC_APmG0?type=png)](https://mermaid.live/edit#pako:eNqVVLFugzAQ_RXLE22ToStDp45ph3ZFshx8JFaMjexzmqjKv_fAkAIpVcuCeff8jnu-8ycvnQKe89LIEJ613HlZF5bRo7SHErWzbPOWkI7DXmnDZwIYWx-licByJu35ilk4IUEt8Yo1Ho7axTDBL2PdZxe3BjbaHkBtdMDvHAGlvxEsow_Oz1Eba-EqAQZqsNhm0xav0VqehAG7w_0sIMTOicr5D-mVOIjGBd1WHrJDIt5RFgtT-laWh__w0YmukGwhCFbdhvbSKgNC2wC-zSA-NO4F1A2ehSGTspH_080POiQeiW6dM2O8isbcwF0KsQWyAQS568nA3-QTX1YI_h907E34C7N15C-8wf5MWwWndAIrtrzTQ-2O3zXejZt3CFbah4UQdetCpG-7jCrcAQ65fyAu_PSUWzqLkqqcyU1OjfCFOtrIkINGYiYyav6OOXTmXCE15RxNM5RNZRpPX6kpx373Mz6fblbwx4Kz9fqJVve0aseYr3gNvpZa0Y3UzX_BcU-eFjynpYJKRoMFL-yFqDKiez_bkufoI6x4bJRE6O8wnlfSBEJBaXT-pb_l2tflC_APmG0)

## Atributos Node

- value - Valor guardado dentro do Node.
- next - Ponteiro para o elemento sucessor do atual. Caso o elemento atual seja o último da lista, o sucessor dele é o primeiro da lista.
- previous - Ponteiro para o elemento antecessor do atual. Caso o elemento atual seja o primeiro da lista, o antecessor dele é o último da lista.

Esses casos especiais dos atributos next e previous caracterizam a lista como sendo uma lista duplamente encadeada circular.

## Atributos DoubleLinkedList

- start - Ponteiro para o Node que está no começo da lista.
- cursor - Ponteiro para algum Node da lista. Seu propósito é facilitar a implementação das operações sobre a lista.
- num_of_elements - Número de elementos da lista.
- max_length - Número de elementos máximo da lista.

## Métodos

### Métodos que manipulam o cursor

Os métodos go_forward_k_positions, go_backward_k_positions, go_to_start e go_to_end têm como objetivo exclusivo manipularem o cursor. Portanto, eles são privados, impedindo com que o usuário manipule o cursor diretamente.

### Métodos de inserção

#### insert_before_current e insert_after_current

Esses métodos permitem que o usuário insira um elemento antes do cursor e depois do cursor, respectivamente. Ambos levantam exceções caso a lista esteja cheia ou vazia (não tem cursor). É importante ressaltar que esses métodos e os que manipulam o cursor servem como base para a implementação dos outros métodos de inserção.

#### \_\_handle_insertion_with_empty_list

Esse é um método privado que é utilizado para tratar o caso especial de inserção de um elemento quando a lista está vazia. É preciso fazer com que os atributos start e cursor apontem para o Node recém criado, além de fazer com que o sucessor e o antecessor do elemento apontem para ele mesmo.

#### insert_at_start

Método para inserção de um elemento no começo da lista. Se ela está cheia, então uma exceção é levantada. Caso ela esteja vazia, é chamado o método \_\_handle_insertion_with_empty_list. Caso contrário, o cursor é movido para o começo da lista e é chamado o método insert_before_current.

#### insert_at_end

Método para inserção de um elemento no final da lista. Se ela está cheia, então uma exceção é levantada. Caso ela esteja vazia, é chamado o método \_\_handle_insertion_with_empty_list. Caso contrário, o cursor é movido para o final da lista e é chamado o método insert_after_current.

#### insert_at_positon

Método para inserção de um elemento em uma dada posição da lista. Se a posição passada como parâmetro for menor do que 1 ou maior do que o número de elementos da lista mais 1, então uma exceção é levantada. Caso a posição seja igual a 1, é chamado o método insert_at_start. Caso a posição seja igual ao número de elementos mais 1, é chamado o método insert_at_end. Caso contrário, o cursor é movido para o começo da lista. Após isso, ele avança posição - 1 posições. Assim, o elemento é inserido antes do cursor, através do método insert_before_current.

### Métodos de remoção

#### remove_current

Remove e retorna o elemento que o cursor está apontando. Após a remoção, o cursor passa a apontar para o antecessor do elemento removido. Porém, se o elemento que foi removido era o primeiro da lista, então o cursor passa a apontar para o sucessor do elemento removido. Levanta exceção caso a lista esteja vazia.

#### remove_first

Remove e retorna o primeiro elemento da lista. Se a lista está vazia, então é levantada uma exceção. Caso contrário o método \_\_go_to_start e remove_current são executados.

#### remove_last

Remove e retorna o último elemento da lista. Se a lista está vazia, então é levantada uma exceção. Caso contrário o método \_\_go_to_end e remove_current são executados.

#### remove_element

Remove e retorna um dado elemento da lista. O método contains é chamado para verificar se o elemento está ou não presente. Se não estiver, então uma exceção é levantada. Caso contrário, é executado o método remove_current.

#### remove_at_position

Remove e retorna o elemento que está em uma dada posição da lista. Se a posição passada como parâmetro for menor do que 1 ou maior do que o número de elementos da lista, então uma exceção é levantada. Caso a posição seja igual a 1, é chamado o método remove_first. Caso a posição seja igual ao número de elementos, é chamado o método remove_last. Caso contrário,
o cursor vai para o começo da lista e avança posição - 1 posições. Após isso, é executado o método remove_current.

### Outros métodos

#### contains

Retorna um valor booleano indicando se um dado elemento está na lista. Percorre a lista procurando o elemento alvo. Se não encontrou, move o cursor para o início e retorna False. Se encontrou, deixa o cursor apontando para o elemento alvo e retorna True.

#### get_position_of

Retorna a posição de um elemento alvo na lista. Percorre a lista procurando o elemento alvo com um contador que vai sendo incrementado por um a cada iteração. Se não encontrou o elemento, levanta uma exceção. Se encontrou, deixa o cursor apontando para o elemento alvo e retorna o valor do contador.

#### get_start, get_end, get_current, get_length e print_list

Os quatro primeiros métodos retornam o primeiro elemento, o último, o cursor e a quantidade de elementos da lista, respectivamente. Já o print_list percorre a lista, pegando os dados de cada Node e executa a função print com os dados coletados. Após a execução desse método, o cursor passa a ser o último elemento da lista.
