# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 4:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 370 windows, 10030 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 190 | 37.9 | 36.5 | $+5.78 | +0.3% | $1005.78 | +0.0 | Sat 9:45 PM | too few trades (190/200) |
| value_ev10 | 487 | 40.9 | 40.4 | $-106.39 | -2.2% | $893.61 | -0.4 | done | can't tell from luck |
| value_ev5 | 719 | 42.1 | 42.1 | $-246.26 | -3.4% | $753.74 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 830 | 49.6 | 49.8 | $-382.37 | -4.6% | $617.63 | -1.3 | done | can't tell from luck |
| trend_filter | 554 | 48.9 | 50.5 | $-408.83 | -7.4% | $591.17 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 999 | 51.6 | 52.1 | $-500.75 | -5.0% | $499.25 | -1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 830 | 50.4 | 52.0 | $-588.39 | -7.1% | $411.61 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 999 | 48.4 | 49.7 | $-603.32 | -6.0% | $396.68 | -1.9 | done | can't tell from luck |
| coinflip | 1474 | 49.8 | 50.8 | $-824.97 | -5.6% | $175.03 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1474 | 49.6 | 51.5 | $-1066.06 | -7.2% | $-66.06 | -2.9 | done | losing for real |
| always_up | 1474 | 45.7 | 50.7 | $-1990.07 | -13.5% | $-990.07 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2251 | 47.4 | 49.4 | $-1773.68 |
| ETH | 2526 | 47.7 | 48.9 | $-1780.96 |
| SOL | 2594 | 48.0 | 49.4 | $-1858.06 |
| XRP | 2659 | 48.8 | 49.1 | $-1298.94 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
