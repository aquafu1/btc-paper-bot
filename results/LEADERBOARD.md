# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 8:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1250 windows, 33896 settled trades, 416 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 665 | 34.1 | 35.3 | $-524.16 | -7.9% | $475.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1625 | 38.4 | 39.2 | $-910.67 | -5.6% | $89.33 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3398 | 50.8 | 50.3 | $-1092.03 | -3.2% | $-92.03 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2841 | 49.5 | 49.4 | $-1334.19 | -4.7% | $-334.19 | -2.5 | done | losing for real |
| value_ev5 | 2454 | 40.2 | 41.1 | $-1374.24 | -5.6% | $-374.24 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2841 | 50.5 | 51.1 | $-1653.74 | -5.8% | $-653.74 | -3.2 | done | losing for real |
| trend_filter | 2004 | 48.7 | 50.4 | $-1712.33 | -8.5% | $-712.33 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3398 | 49.2 | 50.2 | $-2124.15 | -6.3% | $-1124.15 | -3.7 | done | losing for real |
| coinflip | 4890 | 50.0 | 50.1 | $-2215.22 | -4.5% | $-1215.22 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4890 | 50.3 | 51.4 | $-2939.93 | -6.0% | $-1939.93 | -4.3 | done | losing for real |
| always_up | 4890 | 47.9 | 49.3 | $-3607.12 | -7.4% | $-2607.12 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7976 | 48.0 | 48.9 | $-4801.06 |
| ETH | 8610 | 48.1 | 48.3 | $-5102.50 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
