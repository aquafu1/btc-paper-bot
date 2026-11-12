# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 11:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 119 windows, 3039 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 225 | 60.9 | 53.0 | $+282.83 | +12.6% | $1282.83 | +2.0 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 289 | 56.1 | 51.8 | $+174.19 | +6.0% | $1174.19 | +1.1 | done | can't tell from luck |
| momentum_5m_0.00pct | 469 | 52.2 | 50.9 | $-65.14 | -1.4% | $934.86 | -0.3 | done | can't tell from luck |
| value_ev10 | 160 | 38.8 | 40.3 | $-138.93 | -8.7% | $861.07 | -0.9 | Thu 7:15 AM | too few trades (160/200) |
| value_ev20 | 61 | 26.2 | 36.4 | $-182.65 | -29.9% | $817.35 | -1.9 | Sun 12:15 AM | too few trades (61/200) |
| coinflip | 469 | 50.3 | 51.1 | $-271.14 | -5.8% | $728.86 | -1.3 | done | can't tell from luck |
| trend_filter | 157 | 41.4 | 48.9 | $-287.32 | -18.3% | $712.68 | -2.3 | Thu 8:15 AM | too few trades (157/200) |
| value_ev5 | 226 | 38.1 | 41.9 | $-300.08 | -13.3% | $699.92 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 289 | 43.9 | 50.2 | $-441.09 | -15.3% | $558.91 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 225 | 39.1 | 49.1 | $-503.19 | -22.4% | $496.81 | -3.4 | done | losing for real |
| always_up | 469 | 45.4 | 50.2 | $-636.68 | -13.6% | $363.32 | -3.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 652 | 45.6 | 49.6 | $-651.37 |
| ETH | 742 | 45.0 | 48.8 | $-809.68 |
| SOL | 809 | 48.2 | 48.5 | $-580.95 |
| XRP | 836 | 49.8 | 48.8 | $-327.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
