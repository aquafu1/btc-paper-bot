# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 8:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1299 windows, 34650 settled trades, 422 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 683 | 34.3 | 35.3 | $-516.32 | -7.6% | $483.68 | -1.5 | done | can't tell from luck |
| value_ev10 | 1671 | 38.8 | 39.2 | $-753.35 | -4.5% | $246.65 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3476 | 50.8 | 50.2 | $-1050.94 | -3.0% | $-50.94 | -1.8 | done | can't tell from luck |
| value_ev5 | 2519 | 40.5 | 41.1 | $-1231.03 | -4.9% | $-231.03 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2905 | 49.5 | 49.4 | $-1327.76 | -4.6% | $-327.76 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2905 | 50.5 | 51.0 | $-1619.16 | -5.6% | $-619.16 | -3.1 | done | losing for real |
| trend_filter | 2051 | 48.9 | 50.4 | $-1659.32 | -8.1% | $-659.32 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3476 | 49.2 | 50.3 | $-2158.35 | -6.2% | $-1158.35 | -3.7 | done | losing for real |
| coinflip | 4988 | 50.0 | 50.1 | $-2228.53 | -4.5% | $-1228.53 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4988 | 50.4 | 51.4 | $-2831.42 | -5.7% | $-1831.42 | -4.1 | done | losing for real |
| always_up | 4988 | 47.9 | 49.3 | $-3534.77 | -7.1% | $-2534.77 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8342 | 48.0 | 48.8 | $-4748.16 |
| ETH | 8998 | 48.3 | 48.2 | $-4578.55 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
