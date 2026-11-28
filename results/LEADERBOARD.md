# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 6:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1624 windows, 39035 settled trades, 356 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 825 | 34.3 | 35.2 | $-634.04 | -7.7% | $365.96 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3848 | 50.8 | 50.0 | $-1024.52 | -2.7% | $-24.52 | -1.6 | done | can't tell from luck |
| value_ev10 | 1954 | 38.3 | 39.0 | $-1127.37 | -5.8% | $-127.37 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3218 | 51.1 | 50.9 | $-1475.66 | -4.6% | $-475.66 | -2.7 | done | losing for real |
| value_ev5 | 2922 | 40.3 | 41.0 | $-1557.78 | -5.3% | $-557.78 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 3218 | 48.9 | 49.2 | $-1751.56 | -5.4% | $-751.56 | -3.1 | done | losing for real |
| trend_filter | 2288 | 48.5 | 50.4 | $-2045.73 | -8.9% | $-1045.73 | -4.4 | done | losing for real |
| coinflip | 5638 | 50.1 | 49.9 | $-2335.55 | -4.1% | $-1335.55 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3848 | 49.2 | 50.2 | $-2345.19 | -6.1% | $-1345.19 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5638 | 50.2 | 51.3 | $-3464.96 | -6.1% | $-2464.96 | -4.7 | done | losing for real |
| always_up | 5638 | 48.2 | 49.1 | $-3617.39 | -6.4% | $-2617.39 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10429 | 47.9 | 48.6 | $-5922.82 |
| ETH | 11296 | 48.0 | 47.7 | $-5872.71 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
