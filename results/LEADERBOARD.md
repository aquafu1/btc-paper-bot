# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 8:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1009 windows, 28078 settled trades, 76 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 518 | 34.2 | 35.0 | $-312.56 | -6.0% | $687.44 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2419 | 50.3 | 49.7 | $-862.03 | -3.6% | $137.97 | -1.8 | done | can't tell from luck |
| value_ev10 | 1283 | 37.5 | 39.1 | $-922.99 | -7.2% | $77.01 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2863 | 50.9 | 50.4 | $-955.32 | -3.3% | $44.68 | -1.8 | done | can't tell from luck |
| trend_filter | 1684 | 49.9 | 50.8 | $-1121.58 | -6.7% | $-121.58 | -2.8 | done | losing for real |
| value_ev5 | 1945 | 39.6 | 41.0 | $-1274.73 | -6.6% | $-274.73 | -2.4 | done | losing for real |
| coinflip | 4028 | 50.4 | 50.4 | $-1674.37 | -4.2% | $-674.37 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2419 | 49.7 | 51.0 | $-1802.52 | -7.5% | $-802.52 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 2863 | 49.1 | 50.3 | $-1834.69 | -6.4% | $-834.69 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 4028 | 50.7 | 51.5 | $-2213.09 | -5.5% | $-1213.09 | -3.6 | done | losing for real |
| always_up | 4028 | 47.3 | 49.5 | $-3597.40 | -8.9% | $-2597.40 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6403 | 48.3 | 49.0 | $-3510.59 |
| ETH | 6975 | 48.1 | 48.5 | $-4399.55 |
| SOL | 7338 | 48.3 | 48.6 | $-4079.68 |
| XRP | 7362 | 48.1 | 48.4 | $-4581.47 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
