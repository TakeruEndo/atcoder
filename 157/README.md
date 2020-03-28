# Pythonのlistは時間がかかる？
setがlistよりも早い  
- [Pythonで"in list"から"in set"に変えただけで爆速になった件とその理由](https://qiita.com/kitadakyou/items/6f877edd263f097e78f4)
>本当に紛らわしいと思いますが、Python の list は連結リスト構造ではないです。
>基本的には C++ の std::vector と本質的に同じで、list の中身は可変長配列として実装されているはずです。
>連結リスト構造と、可変長配列の、大きな違いとしては、ランダムアクセスに対する性能が大きく異なります。もし Python の list が連結リスト構造ならば、a[i] といったアクセスに O(N)O(N) かかることになりますが、実際は O(1)O(1) で済みます。

- [計算量の話](https://qiita.com/drken/items/18b3b3db5735241465ef)

## E問題解法
set(平衡二分探索木)を使ってlog(n)の計算量で求められ

### 配列２分法アルゴリズム
#### biect
https://docs.python.org/ja/3/library/bisect.html
- [Pythonの配列でC++のstlのupper_boundやlower_bound みたいなことをやるには](http://lilylila.hatenablog.com/entry/20120211/1328925628)
