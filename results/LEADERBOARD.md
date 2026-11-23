# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 5:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1190 windows, 32890 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 641 | 34.9 | 35.3 | $-358.79 | -5.6% | $641.21 | -1.1 | done | can't tell from luck |
| value_ev10 | 1565 | 38.7 | 39.2 | $-780.13 | -5.0% | $219.87 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3292 | 50.9 | 50.3 | $-1029.67 | -3.1% | $-29.67 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2763 | 49.6 | 49.4 | $-1212.74 | -4.4% | $-212.74 | -2.3 | done | losing for real |
| value_ev5 | 2369 | 40.3 | 41.1 | $-1277.04 | -5.4% | $-277.04 | -2.2 | done | losing for real |
| trend_filter | 1943 | 48.8 | 50.5 | $-1627.32 | -8.4% | $-627.32 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2763 | 50.4 | 51.1 | $-1701.96 | -6.2% | $-701.96 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3292 | 49.1 | 50.2 | $-2055.75 | -6.2% | $-1055.75 | -3.6 | done | losing for real |
| coinflip | 4754 | 50.1 | 50.2 | $-2089.47 | -4.4% | $-1089.47 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4754 | 50.1 | 51.4 | $-3034.88 | -6.4% | $-2034.88 | -4.5 | done | losing for real |
| always_up | 4754 | 47.9 | 49.3 | $-3469.78 | -7.3% | $-2469.78 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7553 | 48.2 | 48.9 | $-4175.49 |
| ETH | 8153 | 48.0 | 48.4 | $-5012.15 |
| SOL | 8560 | 48.2 | 48.4 | $-4351.22 |
| XRP | 8624 | 48.1 | 48.2 | $-5098.67 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
