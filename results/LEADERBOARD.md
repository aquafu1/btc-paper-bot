# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 5:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1574 windows, 38397 settled trades, 399 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 803 | 34.4 | 35.2 | $-584.34 | -7.3% | $415.66 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3797 | 50.9 | 50.0 | $-962.00 | -2.5% | $38.00 | -1.6 | done | can't tell from luck |
| value_ev10 | 1902 | 38.5 | 39.0 | $-976.75 | -5.1% | $23.25 | -1.8 | done | can't tell from luck |
| value_ev5 | 2856 | 40.4 | 41.0 | $-1426.13 | -5.0% | $-426.13 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3183 | 51.0 | 50.9 | $-1493.91 | -4.7% | $-493.91 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3183 | 49.0 | 49.2 | $-1687.95 | -5.3% | $-687.95 | -3.0 | done | losing for real |
| trend_filter | 2262 | 48.5 | 50.3 | $-1981.52 | -8.8% | $-981.52 | -4.3 | done | losing for real |
| momentum_15m_0.10pct | 3797 | 49.1 | 50.2 | $-2369.09 | -6.2% | $-1369.09 | -3.9 | done | losing for real |
| coinflip | 5538 | 50.0 | 49.9 | $-2393.06 | -4.3% | $-1393.06 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5538 | 50.1 | 51.3 | $-3528.45 | -6.4% | $-2528.45 | -4.9 | done | losing for real |
| always_up | 5538 | 48.2 | 49.2 | $-3561.59 | -6.4% | $-2561.59 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10143 | 47.9 | 48.6 | $-5761.42 |
| ETH | 10944 | 48.0 | 47.7 | $-5619.13 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
