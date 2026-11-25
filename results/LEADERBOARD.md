# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 6:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1385 windows, 35872 settled trades, 402 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 721 | 34.5 | 35.3 | $-507.53 | -7.0% | $492.47 | -1.4 | done | can't tell from luck |
| value_ev10 | 1743 | 38.8 | 39.1 | $-786.58 | -4.5% | $213.42 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3582 | 50.8 | 50.1 | $-1068.41 | -3.0% | $-68.41 | -1.8 | done | can't tell from luck |
| value_ev5 | 2623 | 40.5 | 41.1 | $-1283.09 | -4.9% | $-283.09 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3006 | 49.3 | 49.3 | $-1478.10 | -4.9% | $-478.10 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3006 | 50.7 | 50.9 | $-1554.02 | -5.2% | $-554.02 | -2.9 | done | losing for real |
| trend_filter | 2129 | 48.5 | 50.4 | $-1883.82 | -8.8% | $-883.82 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3582 | 49.2 | 50.2 | $-2179.81 | -6.1% | $-1179.81 | -3.7 | done | losing for real |
| coinflip | 5160 | 50.0 | 50.0 | $-2218.73 | -4.3% | $-1218.73 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5160 | 50.1 | 51.3 | $-3207.53 | -6.2% | $-2207.53 | -4.6 | done | losing for real |
| always_up | 5160 | 47.8 | 49.3 | $-3740.85 | -7.2% | $-2740.85 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8943 | 47.9 | 48.8 | $-5086.74 |
| ETH | 9619 | 48.1 | 48.1 | $-5237.49 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
