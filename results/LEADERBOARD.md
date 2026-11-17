# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 4:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 657 windows, 18155 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1537 | 50.5 | 49.7 | $-409.39 | -2.7% | $590.61 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1861 | 51.5 | 50.9 | $-530.60 | -2.9% | $469.40 | -1.2 | done | can't tell from luck |
| trend_filter | 1052 | 50.3 | 51.0 | $-587.23 | -5.6% | $412.77 | -1.9 | done | can't tell from luck |
| value_ev10 | 838 | 38.2 | 39.5 | $-615.05 | -7.3% | $384.95 | -1.8 | done | can't tell from luck |
| value_ev5 | 1266 | 40.8 | 41.4 | $-690.41 | -5.5% | $309.59 | -1.7 | done | can't tell from luck |
| coinflip | 2620 | 50.1 | 50.5 | $-1173.74 | -4.5% | $-173.74 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1537 | 49.5 | 51.3 | $-1190.45 | -7.7% | $-190.45 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 1861 | 48.5 | 50.0 | $-1278.17 | -6.9% | $-278.17 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2620 | 50.8 | 51.8 | $-1422.12 | -5.4% | $-422.12 | -2.9 | done | losing for real |
| always_up | 2620 | 47.4 | 49.7 | $-2234.08 | -8.5% | $-1234.08 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4119 | 48.3 | 49.3 | $-2495.32 |
| ETH | 4529 | 48.3 | 48.7 | $-2756.10 |
| SOL | 4725 | 48.1 | 48.8 | $-2861.62 |
| XRP | 4782 | 48.5 | 48.6 | $-2285.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
