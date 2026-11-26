# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 3:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1471 windows, 37080 settled trades, 340 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 750 | 34.0 | 35.4 | $-633.47 | -8.4% | $366.53 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3696 | 50.9 | 50.1 | $-987.93 | -2.7% | $12.07 | -1.6 | done | can't tell from luck |
| value_ev10 | 1807 | 38.4 | 39.2 | $-1000.25 | -5.5% | $-0.25 | -1.9 | done | can't tell from luck |
| value_ev5 | 2724 | 40.3 | 41.1 | $-1471.14 | -5.4% | $-471.14 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3102 | 49.2 | 49.2 | $-1528.05 | -4.9% | $-528.05 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3102 | 50.8 | 51.0 | $-1600.64 | -5.2% | $-600.64 | -2.9 | done | losing for real |
| trend_filter | 2201 | 48.7 | 50.3 | $-1875.16 | -8.5% | $-875.16 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3696 | 49.1 | 50.2 | $-2312.21 | -6.3% | $-1312.21 | -3.8 | done | losing for real |
| coinflip | 5334 | 49.9 | 50.0 | $-2410.67 | -4.5% | $-1410.67 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5334 | 50.1 | 51.3 | $-3363.57 | -6.3% | $-2363.57 | -4.7 | done | losing for real |
| always_up | 5334 | 48.1 | 49.2 | $-3536.76 | -6.6% | $-2536.76 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9529 | 48.0 | 48.7 | $-5266.90 |
| ETH | 10241 | 47.9 | 48.0 | $-5868.73 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
