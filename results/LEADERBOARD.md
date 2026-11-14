# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 7:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 332 windows, 8843 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 705 | 53.5 | 51.7 | $-55.73 | -0.8% | $944.27 | -0.2 | done | can't tell from luck |
| value_ev20 | 175 | 36.0 | 36.6 | $-103.62 | -5.9% | $896.38 | -0.6 | Sat 7:15 PM | too few trades (175/200) |
| reversal_15m_0.10pct | 875 | 53.0 | 52.0 | $-189.39 | -2.2% | $810.61 | -0.7 | done | can't tell from luck |
| value_ev10 | 429 | 38.7 | 40.3 | $-333.92 | -7.8% | $666.08 | -1.4 | done | can't tell from luck |
| value_ev5 | 638 | 40.4 | 42.0 | $-495.35 | -7.8% | $504.65 | -1.7 | done | can't tell from luck |
| coinflip | 1320 | 50.1 | 50.9 | $-736.71 | -5.6% | $263.29 | -2.1 | done | losing for real |
| trend_filter | 481 | 44.7 | 50.3 | $-753.78 | -15.7% | $246.22 | -3.5 | done | losing for real |
| momentum_60m_0.30pct | 705 | 46.5 | 50.0 | $-812.38 | -11.5% | $187.62 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 875 | 47.0 | 49.8 | $-859.69 | -9.8% | $140.31 | -2.9 | done | losing for real |
| always_up | 1320 | 47.7 | 50.3 | $-1199.62 | -9.1% | $-199.62 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1320 | 48.2 | 51.3 | $-1303.31 | -9.9% | $-303.31 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1973 | 46.6 | 49.3 | $-1838.95 |
| ETH | 2217 | 47.1 | 48.7 | $-1899.27 |
| SOL | 2307 | 47.8 | 49.3 | $-1846.68 |
| XRP | 2346 | 48.7 | 49.0 | $-1258.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
