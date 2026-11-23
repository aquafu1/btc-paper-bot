# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 9:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1207 windows, 33257 settled trades, 203 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 649 | 34.5 | 35.3 | $-438.79 | -6.8% | $561.21 | -1.3 | done | can't tell from luck |
| value_ev10 | 1590 | 38.7 | 39.2 | $-794.81 | -5.0% | $205.19 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3333 | 50.8 | 50.3 | $-1105.29 | -3.3% | $-105.29 | -1.9 | done | can't tell from luck |
| value_ev5 | 2403 | 40.4 | 41.1 | $-1230.49 | -5.1% | $-230.49 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2787 | 49.4 | 49.4 | $-1335.79 | -4.8% | $-335.79 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2787 | 50.6 | 51.1 | $-1606.40 | -5.8% | $-606.40 | -3.1 | done | losing for real |
| trend_filter | 1963 | 48.6 | 50.4 | $-1710.37 | -8.7% | $-710.37 | -4.0 | done | losing for real |
| momentum_15m_0.10pct | 3333 | 49.2 | 50.2 | $-2033.43 | -6.1% | $-1033.43 | -3.6 | done | losing for real |
| coinflip | 4804 | 50.1 | 50.1 | $-2152.47 | -4.5% | $-1152.47 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4804 | 50.2 | 51.4 | $-2930.33 | -6.1% | $-1930.33 | -4.4 | done | losing for real |
| always_up | 4804 | 47.9 | 49.3 | $-3452.52 | -7.2% | $-2452.52 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7664 | 48.1 | 48.9 | $-4286.53 |
| ETH | 8283 | 48.1 | 48.3 | $-4919.93 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
