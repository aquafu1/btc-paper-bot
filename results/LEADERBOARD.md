# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 4:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1377 windows, 35762 settled trades, 422 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 714 | 34.2 | 35.3 | $-567.28 | -7.9% | $432.72 | -1.6 | done | can't tell from luck |
| value_ev10 | 1734 | 38.7 | 39.1 | $-826.33 | -4.8% | $173.67 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3574 | 50.8 | 50.1 | $-1057.41 | -3.0% | $-57.41 | -1.8 | done | can't tell from luck |
| value_ev5 | 2612 | 40.4 | 41.1 | $-1338.42 | -5.1% | $-338.42 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2998 | 50.8 | 50.9 | $-1504.42 | -5.0% | $-504.42 | -2.8 | done | losing for real |
| momentum_60m_0.30pct | 2998 | 49.2 | 49.4 | $-1523.06 | -5.1% | $-523.06 | -2.8 | done | losing for real |
| trend_filter | 2126 | 48.4 | 50.4 | $-1907.96 | -9.0% | $-907.96 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3574 | 49.2 | 50.2 | $-2183.92 | -6.1% | $-1183.92 | -3.7 | done | losing for real |
| coinflip | 5144 | 50.0 | 50.0 | $-2238.95 | -4.4% | $-1238.95 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5144 | 50.1 | 51.3 | $-3223.22 | -6.3% | $-2223.22 | -4.6 | done | losing for real |
| always_up | 5144 | 47.9 | 49.3 | $-3695.26 | -7.2% | $-2695.26 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8882 | 47.9 | 48.8 | $-5213.15 |
| ETH | 9570 | 48.0 | 48.1 | $-5268.85 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
