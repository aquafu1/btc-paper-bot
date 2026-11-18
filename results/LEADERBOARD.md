# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 5:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 711 windows, 19609 settled trades, 46 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 373 | 34.0 | 34.9 | $-254.03 | -6.8% | $745.97 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2011 | 51.6 | 50.8 | $-506.58 | -2.5% | $493.42 | -1.1 | done | can't tell from luck |
| value_ev10 | 903 | 38.3 | 39.1 | $-522.57 | -5.8% | $477.43 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 1649 | 50.2 | 49.5 | $-533.19 | -3.2% | $466.81 | -1.3 | done | can't tell from luck |
| value_ev5 | 1360 | 40.9 | 41.1 | $-585.69 | -4.3% | $414.31 | -1.3 | done | can't tell from luck |
| trend_filter | 1142 | 50.3 | 50.9 | $-637.95 | -5.6% | $362.05 | -1.9 | done | can't tell from luck |
| coinflip | 2837 | 50.3 | 50.3 | $-1175.79 | -4.1% | $-175.79 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1649 | 49.8 | 51.3 | $-1229.69 | -7.5% | $-229.69 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2837 | 51.1 | 51.8 | $-1412.69 | -5.0% | $-412.69 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2011 | 48.4 | 50.0 | $-1428.15 | -7.1% | $-428.15 | -3.2 | done | losing for real |
| always_up | 2837 | 47.3 | 49.5 | $-2408.72 | -8.5% | $-1408.72 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4444 | 48.2 | 49.1 | $-2645.40 |
| ETH | 4876 | 48.4 | 48.5 | $-2723.84 |
| SOL | 5114 | 48.2 | 48.7 | $-2874.59 |
| XRP | 5175 | 48.6 | 48.4 | $-2451.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
