# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 7:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1199 windows, 33127 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 647 | 34.6 | 35.3 | $-418.79 | -6.5% | $581.21 | -1.3 | done | can't tell from luck |
| value_ev10 | 1582 | 38.6 | 39.2 | $-807.34 | -5.1% | $192.66 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3320 | 50.8 | 50.3 | $-1113.92 | -3.4% | $-113.92 | -1.9 | done | can't tell from luck |
| value_ev5 | 2393 | 40.4 | 41.1 | $-1246.14 | -5.2% | $-246.14 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2774 | 49.5 | 49.4 | $-1289.44 | -4.6% | $-289.44 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2774 | 50.5 | 51.1 | $-1652.87 | -6.0% | $-652.87 | -3.2 | done | losing for real |
| trend_filter | 1953 | 48.6 | 50.5 | $-1694.02 | -8.7% | $-694.02 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3320 | 49.2 | 50.2 | $-2023.76 | -6.1% | $-1023.76 | -3.6 | done | losing for real |
| coinflip | 4788 | 50.1 | 50.1 | $-2112.77 | -4.4% | $-1112.77 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4788 | 50.2 | 51.4 | $-2972.63 | -6.2% | $-1972.63 | -4.4 | done | losing for real |
| always_up | 4788 | 47.9 | 49.3 | $-3477.04 | -7.3% | $-2477.04 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7603 | 48.1 | 48.9 | $-4275.06 |
| ETH | 8214 | 48.1 | 48.4 | $-4949.42 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
