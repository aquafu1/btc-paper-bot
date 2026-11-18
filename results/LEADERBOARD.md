# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 5:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 710 windows, 19570 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 373 | 34.0 | 34.9 | $-254.03 | -6.8% | $745.97 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1644 | 50.2 | 49.5 | $-503.26 | -3.1% | $496.74 | -1.2 | done | can't tell from luck |
| value_ev10 | 903 | 38.3 | 39.1 | $-522.57 | -5.8% | $477.43 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2006 | 51.5 | 50.7 | $-535.06 | -2.7% | $464.94 | -1.2 | done | can't tell from luck |
| value_ev5 | 1359 | 40.8 | 41.1 | $-602.22 | -4.4% | $397.78 | -1.4 | done | can't tell from luck |
| trend_filter | 1139 | 50.3 | 50.9 | $-628.03 | -5.5% | $371.97 | -1.9 | done | can't tell from luck |
| coinflip | 2832 | 50.2 | 50.3 | $-1224.35 | -4.3% | $-224.35 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1644 | 49.8 | 51.3 | $-1258.17 | -7.7% | $-258.17 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2006 | 48.5 | 50.0 | $-1398.23 | -7.0% | $-398.23 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2832 | 51.1 | 51.8 | $-1417.70 | -5.0% | $-417.70 | -2.8 | done | losing for real |
| always_up | 2832 | 47.3 | 49.5 | $-2437.20 | -8.6% | $-1437.20 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4436 | 48.2 | 49.1 | $-2633.47 |
| ETH | 4869 | 48.3 | 48.5 | $-2738.91 |
| SOL | 5107 | 48.2 | 48.7 | $-2894.16 |
| XRP | 5158 | 48.5 | 48.4 | $-2514.27 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
