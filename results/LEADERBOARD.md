# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 11:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1309 windows, 34819 settled trades, 409 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 686 | 34.3 | 35.3 | $-520.82 | -7.6% | $479.18 | -1.5 | done | can't tell from luck |
| value_ev10 | 1679 | 38.8 | 39.2 | $-767.65 | -4.6% | $232.35 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3491 | 50.9 | 50.2 | $-1012.13 | -2.9% | $-12.13 | -1.7 | done | can't tell from luck |
| value_ev5 | 2534 | 40.5 | 41.1 | $-1264.36 | -5.0% | $-264.36 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2922 | 49.4 | 49.4 | $-1374.71 | -4.7% | $-374.71 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2922 | 50.6 | 51.0 | $-1586.11 | -5.4% | $-586.11 | -3.0 | done | losing for real |
| trend_filter | 2067 | 48.8 | 50.5 | $-1721.78 | -8.3% | $-721.78 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3491 | 49.1 | 50.2 | $-2202.99 | -6.3% | $-1202.99 | -3.8 | done | losing for real |
| coinflip | 5009 | 50.0 | 50.1 | $-2278.78 | -4.5% | $-1278.78 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5009 | 50.3 | 51.4 | $-2928.31 | -5.8% | $-1928.31 | -4.3 | done | losing for real |
| always_up | 5009 | 47.9 | 49.3 | $-3640.00 | -7.3% | $-2640.00 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8431 | 48.0 | 48.8 | $-4921.91 |
| ETH | 9078 | 48.2 | 48.2 | $-4791.48 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
