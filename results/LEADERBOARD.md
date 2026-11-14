# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 1:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 356 windows, 9600 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 186 | 37.1 | 36.6 | $-58.35 | -3.1% | $941.65 | -0.3 | Sat 8:15 PM | too few trades (186/200) |
| value_ev10 | 463 | 40.2 | 40.3 | $-191.42 | -4.1% | $808.58 | -0.7 | done | can't tell from luck |
| value_ev5 | 688 | 41.7 | 42.0 | $-320.39 | -4.7% | $679.61 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 953 | 52.2 | 52.0 | $-374.93 | -3.9% | $625.07 | -1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 788 | 51.3 | 52.0 | $-424.80 | -5.4% | $575.20 | -1.6 | done | can't tell from luck |
| trend_filter | 530 | 47.9 | 50.4 | $-492.27 | -9.3% | $507.73 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 788 | 48.7 | 49.7 | $-500.68 | -6.4% | $499.32 | -1.8 | done | can't tell from luck |
| coinflip | 1417 | 50.1 | 50.8 | $-743.13 | -5.2% | $256.87 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 953 | 47.8 | 49.7 | $-744.04 | -7.8% | $255.96 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1417 | 49.3 | 51.5 | $-1119.66 | -7.9% | $-119.66 | -3.1 | done | losing for real |
| always_up | 1417 | 46.4 | 50.6 | $-1720.27 | -12.1% | $-720.27 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2157 | 47.3 | 49.3 | $-1764.38 |
| ETH | 2414 | 47.6 | 48.8 | $-1761.56 |
| SOL | 2487 | 48.0 | 49.4 | $-1850.96 |
| XRP | 2542 | 48.8 | 49.1 | $-1313.04 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
