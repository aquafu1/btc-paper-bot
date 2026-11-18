# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 2:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 746 windows, 20577 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 386 | 33.2 | 34.9 | $-362.66 | -9.4% | $637.34 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2107 | 51.6 | 50.6 | $-499.40 | -2.4% | $500.60 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1739 | 50.1 | 49.6 | $-628.44 | -3.6% | $371.56 | -1.5 | done | can't tell from luck |
| value_ev10 | 940 | 37.7 | 39.1 | $-696.01 | -7.4% | $303.99 | -1.9 | done | can't tell from luck |
| trend_filter | 1212 | 49.9 | 50.9 | $-785.72 | -6.5% | $214.28 | -2.3 | done | losing for real |
| value_ev5 | 1419 | 40.2 | 41.1 | $-859.23 | -6.1% | $140.77 | -1.9 | done | can't tell from luck |
| coinflip | 2976 | 50.3 | 50.3 | $-1240.48 | -4.2% | $-240.48 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1739 | 49.9 | 51.2 | $-1262.73 | -7.3% | $-262.73 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 2107 | 48.4 | 50.1 | $-1556.01 | -7.4% | $-556.01 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2976 | 50.8 | 51.8 | $-1679.09 | -5.6% | $-679.09 | -3.2 | done | losing for real |
| always_up | 2976 | 46.9 | 49.5 | $-2845.54 | -9.6% | $-1845.54 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4662 | 48.1 | 49.1 | $-2975.49 |
| ETH | 5127 | 48.0 | 48.6 | $-3388.86 |
| SOL | 5362 | 48.0 | 48.6 | $-3360.16 |
| XRP | 5426 | 48.5 | 48.5 | $-2690.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
