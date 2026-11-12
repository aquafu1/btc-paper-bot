# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 119 windows, 3033 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 224 | 61.2 | 53.1 | $+292.83 | +13.1% | $1292.83 | +2.1 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 289 | 56.1 | 51.8 | $+174.19 | +6.0% | $1174.19 | +1.1 | done | can't tell from luck |
| momentum_5m_0.00pct | 468 | 52.1 | 50.9 | $-71.32 | -1.5% | $928.68 | -0.3 | done | can't tell from luck |
| value_ev10 | 160 | 38.8 | 40.3 | $-138.93 | -8.7% | $861.07 | -0.9 | Thu 7:00 AM | too few trades (160/200) |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sat 11:30 PM | too few trades (61/200) |
| coinflip | 468 | 50.4 | 51.1 | $-261.14 | -5.6% | $738.86 | -1.3 | done | can't tell from luck |
| trend_filter | 156 | 41.0 | 48.8 | $-293.51 | -18.8% | $706.49 | -2.3 | Thu 8:00 AM | too few trades (156/200) |
| value_ev5 | 226 | 38.1 | 41.9 | $-300.08 | -13.3% | $699.92 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 289 | 43.9 | 50.2 | $-441.09 | -15.3% | $558.91 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 224 | 38.8 | 49.0 | $-509.37 | -22.7% | $490.63 | -3.4 | done | losing for real |
| always_up | 468 | 45.5 | 50.2 | $-626.68 | -13.4% | $373.32 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 652 | 45.6 | 49.6 | $-651.37 |
| ETH | 742 | 45.0 | 48.8 | $-809.68 |
| SOL | 809 | 48.2 | 48.5 | $-580.95 |
| XRP | 830 | 49.8 | 48.8 | $-315.76 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
