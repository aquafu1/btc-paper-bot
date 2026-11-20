# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 7:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 908 windows, 25073 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 470 | 35.1 | 34.8 | $-161.30 | -3.4% | $838.70 | -0.6 | done | can't tell from luck |
| value_ev10 | 1150 | 38.2 | 39.1 | $-633.08 | -5.5% | $366.92 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2122 | 49.9 | 49.8 | $-969.75 | -4.6% | $30.25 | -2.1 | done | losing for real |
| value_ev5 | 1737 | 39.9 | 41.0 | $-1017.46 | -5.9% | $-17.46 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2557 | 50.6 | 50.5 | $-1031.17 | -4.0% | $-31.17 | -2.0 | done | losing for real |
| trend_filter | 1486 | 49.8 | 51.0 | $-1046.14 | -7.0% | $-46.14 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2122 | 50.1 | 50.8 | $-1367.83 | -6.4% | $-367.83 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2557 | 49.4 | 50.3 | $-1407.49 | -5.5% | $-407.49 | -2.8 | done | losing for real |
| coinflip | 3624 | 50.2 | 50.3 | $-1610.39 | -4.4% | $-610.39 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3624 | 51.1 | 51.6 | $-1731.31 | -4.8% | $-731.31 | -3.0 | done | losing for real |
| always_up | 3624 | 46.8 | 49.6 | $-3608.85 | -10.0% | $-2608.85 | -6.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5716 | 48.2 | 49.0 | $-3201.45 |
| ETH | 6234 | 48.2 | 48.5 | $-3842.34 |
| SOL | 6540 | 48.1 | 48.6 | $-3796.11 |
| XRP | 6583 | 48.3 | 48.5 | $-3744.87 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
